# scripts/publish.py
"""
Orchestre les publications/cron du projet, SANS dépendre de notify_block.
- Evite les imports circulaires (import de commands_admin.* à l’intérieur des fonctions).
- Fournit toutes les fonctions attendues par scheduler.py : publier_film, publier_quiz,
  publier_correction, publier_actu_privee, envoyer_statistiques, sauvegarder_donnees,
  publier_meilleurs_abonnes, publier_abonnes_du_mois, publier_anniversaires, + run_all.
- Ne plante pas si certaines briques ne sont pas encore implémentées.
"""

from typing import Optional

# Utilitaires/scripts dispo dans le repo
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


# ---------- Fonctions attendues par scheduler.py ----------

def publier_actu_privee(bot: Optional[object] = None) -> None:
    """
    Placeholder pour l'actu privée. Implémente ici la logique réelle si besoin.
    On évite toute import manquant : on log simplement pour le moment.
    """
    print("📰 publier_actu_privee : placeholder (aucune action).")


def publier_film(bot: Optional[object] = None) -> None:
    """
    Pas de scripts.films dans le projet → on ne tente pas d'importer.
    """
    print("🎬 publier_film : non implémenté (aucun module films dans ce repo).")


def publier_quiz(bot: Optional[object] = None) -> None:
    """
    Pas de scripts.quiz dans le projet → placeholder.
    """
    print("❓ publier_quiz : non implémenté (aucun module quiz dans ce repo).")


def publier_correction(bot: Optional[object] = None) -> None:
    """
    Pas de scripts.correction dans le projet → placeholder.
    """
    print("✅ publier_correction : non implémenté (aucun module correction dans ce repo).")


def publier_meilleurs_abonnes(bot: Optional[object] = None) -> None:
    """
    Utilise scripts.points.publier_meilleurs_abonnes si présent.
    """
    if _publier_top_points is None:
        print("🏅 publier_meilleurs_abonnes : fonction indisponible (scripts.points manquant).")
        return
    try:
        _publier_top_points(bot)
    except TypeError:
        # Si la fonction n'accepte pas bot
        _publier_top_points()
    except Exception as e:
        print(f"⚠️ publier_meilleurs_abonnes a échoué : {e}")


def publier_abonnes_du_mois(bot: Optional[object] = None) -> None:
    """
    Aucune fonction dédiée dans le repo → placeholder.
    """
    print("🎁 publier_abonnes_du_mois : non implémenté.")


def envoyer_statistiques(bot: Optional[object] = None) -> None:
    """
    Aucune fonction dédiée dans le repo → placeholder.
    """
    print("📊 envoyer_statistiques : non implémenté.")


def sauvegarder_donnees(bot: Optional[object] = None) -> None:
    """
    Sauvegarde « logiques » minimales : points utilisateurs si dispo.
    (Le backup ZIP se fait séparément via backup_donnees.)
    """
    if _save_points is None:
        print("💾 sauvegarder_donnees : points_logic indisponible, rien à sauvegarder.")
        return
    try:
        print("💾 sauvegarder_donnees : sauvegarde des points utilisateurs...")
        _save_points()
        print("💾 sauvegarder_donnees : OK.")
    except Exception as e:
        print(f"⚠️ sauvegarder_donnees a échoué : {e}")


def publier_anniversaires(bot: Optional[object] = None) -> None:
    """
    IMPORTANT : on importe ICI (lazy import) pour éviter les imports circulaires :
      main -> commands_admin -> scheduler -> scripts.publish -> ... -> commands_admin
    """
    try:
        from commands_admin.anniversaire import envoyer_anniversaires
    except Exception as e:
        print(f"🎂 publier_anniversaires : impossible d’importer commands_admin.anniversaire ({e})")
        return

    try:
        envoyer_anniversaires(bot)
        print("🎂 publier_anniversaires : messages envoyés (si des anniversaires aujourd’hui).")
    except Exception as e:
        print(f"⚠️ publier_anniversaires a échoué : {e}")


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
    print("🚀 Lancement manuel des publications (run_all)...")

    try:
        publier_actu_privee(bot)
    except Exception as e:
        print(f"⚠️ publier_actu_privee a échoué : {e}")

    try:
        publier_anniversaires(bot)
    except Exception as e:
        print(f"⚠️ publier_anniversaires a échoué : {e}")

    try:
        publier_film(bot)
    except Exception as e:
        print(f"⚠️ publier_film a échoué : {e}")

    try:
        publier_quiz(bot)
    except Exception as e:
        print(f"⚠️ publier_quiz a échoué : {e}")

    try:
        publier_correction(bot)
    except Exception as e:
        print(f"⚠️ publier_correction a échoué : {e}")

    try:
        publier_meilleurs_abonnes(bot)
    except Exception as e:
        print(f"⚠️ publier_meilleurs_abonnes a échoué : {e}")

    try:
        envoyer_statistiques(bot)
    except Exception as e:
        print(f"⚠️ envoyer_statistiques a échoué : {e}")

    try:
        sauvegarder_donnees(bot)
    except Exception as e:
        print(f"⚠️ sauvegarder_donnees a échoué : {e}")

    # Backup ZIP (si dispo)
    if _backup_donnees is not None:
        try:
            print("🗄️ backup_donnees ...")
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
    "publier_film",
    "publier_quiz",
    "publier_correction",
    "publier_meilleurs_abonnes",
    "publier_abonnes_du_mois",
    "envoyer_statistiques",
    "sauvegarder_donnees",
    "publier_anniversaires",
    "run_all",
]

#___Partie notification admin____


import telebot
from datetime import datetime

from commands_adm.anniversaire import get_today_anniversaires, format_anniversaire_message
from scripts.fetch_cinema_news import fetch_cinema_news
from scripts.fetch_anilist_news import fetch_anilist_news
from scripts.notify_sorties import notify_admins_sorties

# Liste des admins
ADMINS = [5618445554, 879386491]

def notifier_admins_daily(bot: telebot.TeleBot):
    """
    Envoie une notification quotidienne aux admins.
    Inclut : anniversaires, actualités cinéma/animation, et rappel des sorties.
    """
    today = datetime.now().strftime("%d/%m/%Y")
    header = f"📌 *Rapport quotidien Geekmania* — {today}\n\n"

    # ---- Anniversaires ----
    anniversaires = get_today_anniversaires()
    if anniversaires:
        anniv_text = "🎉 *Anniversaires du jour :*\n"
        for entry in anniversaires:
            anniv_text += f"- {entry['nom']} ({entry.get('profession', 'Inconnu')})\n"
    else:
        anniv_text = "🎉 Aucun anniversaire enregistré aujourd’hui.\n"

    # ---- Actus Cinéma ----
    cinema_news = fetch_cinema_news()
    if cinema_news:
        cinema_text = "🎬 *Actualités Cinéma :*\n" + "\n".join([f"- {n}" for n in cinema_news[:3]])
    else:
        cinema_text = "🎬 Pas de nouvelles ciné aujourd’hui."

    # ---- Actus Animation ----
    anime_news = fetch_anilist_news()
    if anime_news:
        anime_text = "🌸 *Actualités Animation :*\n" + "\n".join([f"- {n}" for n in anime_news[:3]])
    else:
        anime_text = "🌸 Pas de nouvelles animation aujourd’hui."

    # ---- Sorties à venir ----
    sorties_text = "📅 *Sorties à venir :*\n"
    try:
        sorties_text += notify_admins_sorties(bot, preview=True)
    except Exception:
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

    print("✅ Notification quotidienne envoyée aux admins")