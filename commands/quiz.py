# commands/quiz.py

import os
import json
import random
from datetime import datetime, timedelta
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from telebot import TeleBot

# === Config ===
QUIZZ_FILE = "data/quizz/quizz.json"
QUIZ_LOG_FILE = "data/quiz_log.json"
SYNC_CHAT_ID = os.getenv("@gedajteste", "@GEEKMANI")  # canal/groupe synchronisé
AUTHORIZED_ADMINS = [5618445554, 879386491]

# Points attribués si bonne réponse
POINTS_ON_CORRECT = 5

# --- intégration points: on tente plusieurs fonctions possibles sans planter ---
_add_points_fn = None
try:
    from scripts.points_logic import add_points as _add_points_fn   # si tu as add_points(uid, pts)
except Exception:
    try:
        from scripts.points_logic import ajouter_points as _add_points_fn
    except Exception:
        try:
            from scripts.points_logic import incrementer_points as _add_points_fn
        except Exception:
            try:
                from scripts.points import add_points as _add_points_fn
            except Exception:
                _add_points_fn = None  # pas de fonction dispo, on n'attribue pas (mais on logue)

# === Helpers JSON ===
def _ensure_dirs():
    os.makedirs("data/quizz", exist_ok=True)

def _read_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default

def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# === Chargement quiz ===
def _load_quizzes():
    quizzes = _read_json(QUIZZ_FILE, [])
    # Validation sommaire
    valid = []
    for q in quizzes:
        if isinstance(q, dict) and "question" in q and "options" in q and "correct" in q:
            valid.append(q)
    return valid

def _pick_quiz():
    quizzes = _load_quizzes()
    if not quizzes:
        return None
    return random.choice(quizzes)

# === Log structure ===
def _load_log():
    default = {
        "active": [],   # liste d’objets {quiz_id, chat_id, message_id, posted_at, closes_at, correct, options, explication}
        "answers": [],  # liste d’objets {quiz_id, user_id, username, first_name, option, at}
        "history": []   # liste d’objets {quiz_id, message_id, published_at, revealed_at, correct, winners_count}
    }
    return _read_json(QUIZ_LOG_FILE, default)

def _save_log(log):
    _write_json(QUIZ_LOG_FILE, log)

# === Publication du quiz ===
def _build_keyboard(options):
    # Boutons A/B/C/D…
    labels = ["A", "B", "C", "D", "E", "F"]
    markup = InlineKeyboardMarkup()
    row = []
    for i, opt in enumerate(options):
        label = labels[i] if i < len(labels) else str(i + 1)
        row.append(InlineKeyboardButton(f"{label}", callback_data=f"quiz:{i}"))
        if len(row) == 3:
            markup.row(*row)
            row = []
    if row:
        markup.row(*row)
    return markup

def send_quiz(bot: TeleBot):
    """À appeler par le scheduler (ou manuellement). Choisit un quiz aléatoire et le publie dans le canal/groupe sync."""
    _ensure_dirs()
    quiz = _pick_quiz()
    if not quiz:
        # notifier admins si aucun quiz
        for aid in AUTHORIZED_ADMINS:
            bot.send_message(aid, "⚠️ Aucun quiz disponible dans data/quizz/quizz.json.")
        return

    # Construire le message
    text = "🎬 *Quiz du jour* 🎯\n\n"
    text += f"{quiz['question']}\n\n"
    for i, opt in enumerate(quiz["options"], start=1):
        text += f"{i}. {opt}\n"

    # Envoyer
    markup = _build_keyboard(quiz["options"])
    msg = bot.send_message(SYNC_CHAT_ID, text, parse_mode="Markdown", reply_markup=markup)

    # Logguer comme actif pendant 24h
    now = datetime.now()
    closes = now + timedelta(hours=24)

    log = _load_log()
    # Assigner un quiz_id unique (timestamp + message_id)
    quiz_id = int(now.timestamp())
    log["active"].append({
        "quiz_id": quiz_id,
        "chat_id": msg.chat.id,
        "message_id": msg.message_id,
        "posted_at": now.isoformat(),
        "closes_at": closes.isoformat(),
        "correct": quiz["correct"],
        "options": quiz["options"],
        "explication": quiz.get("explication", "")
    })
    _save_log(log)

def _award_points_safe(user_id, points):
    if _add_points_fn:
        try:
            _add_points_fn(user_id, points)
        except Exception:
            # on ignore si la signature ne correspond pas
            pass

# === Gestion des réponses par boutons ===
def _is_quiz_open(active_entry):
    try:
        return datetime.fromisoformat(active_entry["closes_at"]) > datetime.now()
    except Exception:
        return False

def _get_active_by_message(log, chat_id, message_id):
    for entry in log["active"]:
        if entry["chat_id"] == chat_id and entry["message_id"] == message_id:
            return entry
    return None

def _user_already_answered(log, quiz_id, user_id):
    for a in log["answers"]:
        if a["quiz_id"] == quiz_id and a["user_id"] == user_id:
            return True
    return False

# === Révélation des réponses (scheduler) ===
def reveal_quiz_answers(bot: TeleBot):
    """À appeler par le scheduler (quotidien). Révèle les réponses des quiz échus & attribue les points."""
    _ensure_dirs()
    log = _load_log()
    now = datetime.now()
    still_active = []
    for entry in log["active"]:
        closes_at = datetime.fromisoformat(entry["closes_at"])
        if closes_at <= now:
            # Révéler ce quiz
            correct_idx = entry["correct"]
            correct_label = ["A", "B", "C", "D", "E", "F"][correct_idx] if correct_idx < 6 else str(correct_idx + 1)
            correct_text = entry["options"][correct_idx]

            # Récupérer gagnants
            winners = []
            for ans in log["answers"]:
                if ans["quiz_id"] == entry["quiz_id"] and ans["option"] == correct_idx:
                    winners.append(ans)

            # Attribuer points
            for w in winners:
                _award_points_safe(w["user_id"], POINTS_ON_CORRECT)

            # Message de révélation
            explication = entry.get("explication", "")
            winners_line = "👑 Gagnants: " + (", ".join([w.get("first_name") or w.get("username") or str(w["user_id"]) for w in winners[:15]]) if winners else "aucun 😅")
            text = (
                f"✅ *Réponse du quiz d’hier*\n\n"
                f"Bonne réponse : *{correct_label} — {correct_text}*\n"
            )
            if explication:
                text += f"\nℹ️ {explication}\n"
            text += f"\n{winners_line}\n"
            if winners:
                text += f"\n+{POINTS_ON_CORRECT} points pour chaque bonne réponse 🎉"

            bot.send_message(entry["chat_id"], text, parse_mode="Markdown")

            # Historiser
            log["history"].append({
                "quiz_id": entry["quiz_id"],
                "message_id": entry["message_id"],
                "published_at": entry["posted_at"],
                "revealed_at": now.isoformat(),
                "correct": correct_idx,
                "winners_count": len(winners)
            })
        else:
            still_active.append(entry)

    log["active"] = still_active
    _save_log(log)

# === Handlers à enregistrer ===
def register_quiz(bot: TeleBot):
    _ensure_dirs()

    # 1) Commande admin pour forcer l’envoi du quiz du jour
    @bot.message_handler(commands=["quiz"])
    def cmd_quiz(message: Message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Réservé aux admins.")
            return
        send_quiz(bot)
        bot.reply_to(message, "🎯 Quiz du jour publié.")

    # 2) Réception des réponses via callback (boutons A/B/C/…)
    @bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("quiz:"))
    def on_quiz_answer(call: CallbackQuery):
        # call.message => le message du quiz (dans le canal/groupe)
        # call.from_user => utilisateur qui clique
        if not call.message or not call.message.message_id:
            return
        try:
            chosen = int(call.data.split(":")[1])
        except Exception:
            return

        log = _load_log()
        active = _get_active_by_message(log, call.message.chat.id, call.message.message_id)
        if not active:
            bot.answer_callback_query(call.id, "Ce quiz n’est plus actif.", show_alert=False)
            return

        if not _is_quiz_open(active):
            bot.answer_callback_query(call.id, "Temps écoulé ⌛️", show_alert=False)
            return

        uid = call.from_user.id
        if _user_already_answered(log, active["quiz_id"], uid):
            bot.answer_callback_query(call.id, "Tu as déjà répondu 👌", show_alert=False)
            return

        # Enregistrer la réponse
        log["answers"].append({
            "quiz_id": active["quiz_id"],
            "user_id": uid,
            "username": call.from_user.username or "",
            "first_name": call.from_user.first_name or "",
            "option": chosen,
            "at": datetime.now().isoformat()
        })
        _save_log(log)

        # Accusé réception
        labels = ["A", "B", "C", "D", "E", "F"]
        chosen_label = labels[chosen] if chosen < len(labels) else str(chosen + 1)
        bot.answer_callback_query(call.id, f"Réponse enregistrée: {chosen_label} ✅", show_alert=False)

# === Fonctions exposées pour le scheduler ===
# Dans scheduler.py, appelle:
# - from commands.quiz import send_quiz, reveal_quiz_answers
# - schedule.every().day.at("09:00").do(lambda: send_quiz(bot))
# - schedule.every().day.at("09:00").do(lambda: reveal_quiz_answers(bot))