# scripts/publish.py
"""
Orchestrateur des tâches (cron) SANS notify_block et SANS import circulaire.
- Fournit toutes les fonctions attendues par scheduler.py (même en placeholders).
- N'importe aucune dépendance fragile au niveau global.
"""

from typing import Optional, List
import os

# --- Imports optionnels et sûrs (si absents, on fait des placeholders) ---
try:
    from scripts.points import publier_meilleurs_abonnes as _publier_top_points
except Exception:
    _publier_top_points = None

try:
    from scripts.points_logic import sauvegarder_points_utilisateurs as _save_points
except Exception:
    _save_points = None

try:
    from scripts.backup import backup_donnees as _backup_donnees
except Exception:
    _backup_donnees = None

try:
    from scripts.fetch_cinema_news import fetch_cinema_news as _fetch_cinema_news
except Exception:
    _fetch_cinema_news = None

try:
    from scripts.fetch_anilist_news import fetch_anilist_news as _fetch_anilist_news
except Exception:
    _fetch_anilist_news = None

try:
    from scripts.notify_sorties import notify_admins_sorties as _notify_admins_sorties
except Exception:
    _notify_admins_sorties = None


# --- ADMINS : via variable d'env "ADMINS" (ids séparés par des virgules), sinon fallback ---
def _parse_admins_env() -> List[int]:
    raw = os.getenv("ADMINS", "").strip()
    ids: List[int] = []
    if raw:
        for part in raw.split(","):
            part = part.strip()
            if part.isdigit():
                try:
                    ids.append(int(part))
                except Exception:
                    pass
    return ids

ADMINS: List[int] = _parse_admins_env() or [5618445554, 879386491]


# ---------- Fonctions attendues par scheduler.py (placeholders robustes) ----------

def publier_actu_privee(bot: Optional[object] = None) -> None:
    print("📰 publier_actu_privee : placeholder (aucune action).")


def publier_film(bot: Optional[object] = None) -> None:
    print("🎬 publier_film : non implémenté.")


def publier_quiz(bot: Optional[object] = None) -> None:
    print("❓ publier_quiz : non implémenté.")


def publier_correction(bot: Optional[object] = None) -> None:
    print("✅ publier_correction : non implémenté.")


def publier_meilleurs_abonnes(bot: Optional[object] = None) -> None:
    if _publier_top_points is None:
        print("🏅 publier_meilleurs_abonnes : indisponible (scripts.points manquant).")
        return
    try:
        _publier_top_points(bot)
    except TypeError:
        _publier_top_points()
    except Exception as e:
        print(f"⚠️ publier_meilleurs_abonnes a échoué : {e}")


def publier_abonnes_du_mois(bot: Optional[object] = None) -> None:
    print("🎁 publier_abonnes_du_mois : non implémenté.")


def envoyer_statistiques(bot: Optional[object] = None) -> None:
    print("📊 envoyer_statistiques : non implémenté.")


def sauvegarder_donnees(bot: Optional[object] = None) -> None:
    if _save_points is None:
        print("💾 sauvegarder_donnees : points_logic indisponible, rien à sauvegarder.")
        return
    try:
        print("💾 sauvegarder_donnees : sauvegarde des points utilisateurs…")
        _save_points()
        print("💾 sauvegarder_donnees : OK.")
    except Exception as e:
        print(f"⚠️ sauvegarder_donnees a échoué : {e}")


def publier_anniversaires(bot: Optional[object] = None) -> None:
    """
    Lazy-import pour éviter les imports circulaires :
    essaie d'abord commands_admin.anniversaire puis commands_adm.anniversaire.
    """
    envoyer_anniversaires = None
    last_err = None

    for mod in ("commands_admin.anniversaire", "commands_adm.anniversaire"):
        try:
            module = __import__(mod, fromlist=["envoyer_anniversaires"])
            envoyer_anniversaires = getattr(module, "envoyer_anniversaires", None)
            if envoyer_anniversaires:
                break
        except Exception as e:
            last_err = e

    if not envoyer_anniversaires:
        print(f"🎂 publier_anniversaires : module anniversaire introuvable ({last_err}).")
        return

    try:
        envoyer_anniversaires(bot)
        print("🎂 publier_anniversaires : messages envoyés (si anniversaires).")
    except Exception as e:
        print(f"⚠️ publier_anniversaires a échoué : {e}")


# ---------- Notification quotidienne admins ----------

def notifier_admins_daily(bot: object) -> None:
    """
    Envoie une notification quotidienne aux admins avec :
    - anniversaires du jour (si module présent),
    - 3 actus cinéma (si dispo),
    - 3 actus animation (si dispo),
    - aperçu des sorties (si notify_admins_sorties supporte preview=True).
    """
    from datetime import datetime

    # Récup anniversaires (lazy-import pour éviter cycles)
    anniversaires = []
    get_today_anniversaires = None

    for mod in ("commands_admin.anniversaire", "commands_adm.anniversaire"):
        try:
            module = __import__(mod, fromlist=["get_today_anniversaires"])
            get_today_anniversaires = getattr(module, "get_today_anniversaires", None)
            if get_today_anniversaires:
                anniversaires = get_today_anniversaires() or []
                break
        except Exception:
            pass

    today = datetime.now().strftime("%d/%m/%Y")
    header = f"📌 *Rapport quotidien Geekmania* — {today}\n\n"

    # ---- Anniversaires ----
    if anniversaires:
        anniv_lines = [
            f"- {entry.get('nom', 'Inconnu')} ({entry.get('profession', 'Inconnu')})"
            for entry in anniversaires
        ]
        anniv_text = "🎉 *Anniversaires du jour :*\n" + "\n".join(anniv_lines)
    else:
        anniv_text = "🎉 Aucun anniversaire enregistré aujourd’hui."

    # ---- Actus Cinéma ----
    if _fetch_cinema_news:
        try:
            cinema_news = _fetch_cinema_news() or []
            cinema_text = "🎬 *Actualités Cinéma :*\n" + "\n".join([f"- {n}" for n in cinema_news[:3]]) if cinema_news else "🎬 Pas de nouvelles ciné aujourd’hui."
        except Exception:
            cinema_text = "🎬 Pas de nouvelles ciné aujourd’hui."
    else:
        cinema_text = "🎬 Pas de nouvelles ciné aujourd’hui."

    # ---- Actus Animation ----
    if _fetch_anilist_news:
        try:
            anime_news = _fetch_anilist_news() or []
            anime_text = "🌸 *Actualités Animation :*\n" + "\n".join([f"- {n}" for n in anime_news[:3]]) if anime_news else "🌸 Pas de nouvelles animation aujourd’hui."
        except Exception:
            anime_text = "🌸 Pas de nouvelles animation aujourd’hui."
    else:
        anime_text = "🌸 Pas de nouvelles animation aujourd’hui."

    # ---- Sorties (aperçu) ----
    sorties_text = "📅 *Sorties à venir :*\n"
    if _notify_admins_sorties:
        try:
            preview = _notify_admins_sorties(bot, preview=True)
            if isinstance(preview, str) and preview.strip():
                sorties_text += preview.strip()
            else:
                sorties_text += "Aucune donnée disponible."
        except Exception:
            sorties_text += "Aucune donnée disponible."
    else:
        sorties_text += "Aucune donnée disponible."

    # ---- Construction finale ----
    message = (
        header
        + anniv_text + "\n\n"
        + cinema_text + "\n\n"
        + anime_text + "\n\n"
        + sorties_text
    )

    # ---- Envoi aux admins ----
    for admin_id in ADMINS:
        try:
            bot.send_message(admin_id, message, parse_mode="Markdown")
        except Exception as e:
            print(f"Erreur lors de l’envoi à {admin_id}: {e}")

    print("✅ Notification quotidienne envoyée aux admins.")


# ---------- Exécution manuelle complète ----------

def run_all(bot: Optional[object] = None) -> None:
    """
    Exécute en chaîne les tâches principales. Robuste aux fonctions manquantes.
    Ordre :
      1) Actu privée
      2) Anniversaires
      3) Film
      4) Quiz
      5) Correction
      6) Classements / Stats
      7) Sauvegarde logique + Backup ZIP
    """
    print("🚀 Lancement manuel des publications (run_all)…")

    try: publier_actu_privee(bot)
    except Exception as e: print(f"⚠️ publier_actu_privee a échoué : {e}")

    try: publier_anniversaires(bot)
    except Exception as e: print(f"⚠️ publier_anniversaires a échoué : {e}")

    try: publier_film(bot)
    except Exception as e: print(f"⚠️ publier_film a échoué : {e}")

    try: publier_quiz(bot)
    except Exception as e: print(f"⚠️ publier_quiz a échoué : {e}")

    try: publier_correction(bot)
    except Exception as e: print(f"⚠️ publier_correction a échoué : {e}")

    try: publier_meilleurs_abonnes(bot)
    except Exception as e: print(f"⚠️ publier_meilleurs_abonnes a échoué : {e}")

    try: envoyer_statistiques(bot)
    except Exception as e: print(f"⚠️ envoyer_statistiques a échoué : {e}")

    try: sauvegarder_donnees(bot)
    except Exception as e: print(f"⚠️ sauvegarder_donnees a échoué : {e}")

    if _backup_donnees is not None:
        try:
            print("🗄️ backup_donnees …")
            try:
                _backup_donnees(bot)
            except TypeError:
                _backup_donnees()
        except Exception as e:
            print(f"⚠️ backup_donnees a échoué : {e}")
    else:
        print("🗄️ backup_donnees indisponible (scripts.backup manquant).")

    print("✅ run_all terminé.")


__all__ = [
    "publier_actu_privee",
    "publier_anniversaires",
    "publier_film",
    "publier_quiz",
    "publier_correction",
    "publier_meilleurs_abonnes",
    "publier_abonnes_du_mois",
    "envoyer_statistiques",
    "sauvegarder_donnees",
    "notifier_admins_daily",
    "run_all",
]