# scheduler.py
"""
Planificateur central pour Gedaj.
- Evite les imports circulaires en important les fonctions de publication à l'intérieur de la fonction principale.
- Garantit qu'une tâche programmée ne soit exécutée qu'une fois pour la période attendue (jour/semaine/mois).
- Fournit des logs clairs pour faciliter le debug lors du déploiement.
"""

import logging
import traceback
from datetime import datetime
from time import sleep
from typing import Optional

# Configuration du logger simple (tu peux l'adapter à ton système de logs)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def _date_str():
    return datetime.now().strftime("%Y-%m-%d")


def _week_str():
    y, w, _ = datetime.now().isocalendar()
    return f"{y}-W{w}"


def _month_str():
    return datetime.now().strftime("%Y-%m")


def lancer_taches_scheduled(bot: Optional[object] = None):
    """
    Boucle principale du scheduler.
    Si `bot` est None, on tente de récupérer `loader.bot` (lazy import) — pratique pour l'import depuis main.
    """

    # Récupérer le bot uniquement si nécessaire, et de façon lazy pour éviter les imports circulaires
    if bot is None:
        try:
            from loader import bot as _loader_bot  # lazy import
            bot = _loader_bot
            logging.info("Bot chargé depuis loader.")
        except Exception:
            bot = None
            logging.warning("loader.bot introuvable — les tâches nécessitant le bot seront appelées avec bot=None.")

    # last_run mémorise la dernière "période" (date / semaine / mois) où une tâche a été exécutée.
    last_run = {
        # exemples de clés :
        # 'daily_09': '2025-08-27', 'weekly_sun_20': '2025-W35', 'monthly_1_10': '2025-08'
    }

    logging.info("⏱️ Planificateur en marche...")

    while True:
        now = datetime.now()
        heure = now.strftime("%H:%M")

        # Import lazy des fonctions de publication (pour éviter import circulaire)
        try:
            from scripts.publish import (
                publier_film,
                publier_quiz,
                publier_correction,
                publier_actu_privee,
                envoyer_statistiques,
                publier_meilleurs_abonnes,
                publier_abonnes_du_mois,
                sauvegarder_donnees,
                publier_anniversaires,
                notifier_admins_daily,
            )
        except Exception as e:
            # Si import échoue, on prépare des placeholders qui loggent l'absence
            logging.warning(f"Impossible d'importer scripts.publish complètement : {e}")
            # Définitions fallback pour éviter crash : fonctions qui loggent et ne font rien
            def _missing(name):
                def _fn(*a, **k):
                    logging.warning(f"(missing) {name} appelé mais indisponible.")
                return _fn

            publier_film = _missing("publier_film")
            publier_quiz = _missing("publier_quiz")
            publier_correction = _missing("publier_correction")
            publier_actu_privee = _missing("publier_actu_privee")
            envoyer_statistiques = _missing("envoyer_statistiques")
            publier_meilleurs_abonnes = _missing("publier_meilleurs_abonnes")
            publier_abonnes_du_mois = _missing("publier_abonnes_du_mois")
            sauvegarder_donnees = _missing("sauvegarder_donnees")
            publier_anniversaires = _missing("publier_anniversaires")
            notifier_admins_daily = _missing("notifier_admins_daily")

        # Import lazy backup
        try:
            from scripts.backup import backup_donnees
        except Exception as e:
            logging.warning(f"scripts.backup non disponible : {e}")

            def backup_donnees(*a, **k):
                logging.warning("(missing) backup_donnees appelé mais indisponible.")

        # Helper : exécute une fonction en essayant d'appeler avec bot puis sans (ou inverse),
        # en loggant les exceptions. Retourne True si la fonction a été tentée.
        def _call_task(fn, name, context_key):
            """
            fn : callable
            name : str (pour log)
            context_key : clé à mettre à jour dans last_run pour bloquer ré-execution
            """
            period_marker = None  # valeur qu'on stockera dans last_run (date/week/month)
            try:
                # Déterminer le marqueur de période selon la clé (convention)
                if context_key.startswith("daily_"):
                    period_marker = _date_str()
                elif context_key.startswith("weekly_"):
                    period_marker = _week_str()
                elif context_key.startswith("monthly_"):
                    period_marker = _month_str()
                else:
                    period_marker = _date_str()

                logging.info(f"Exécution tâche: {name} (context: {context_key})")
                # Essayer d'appeler avec bot si possible, sinon sans.
                try:
                    fn(bot)
                except TypeError:
                    # signature peut être fn() ou fn(bot) ; on réessaye sans bot
                    fn()
                except Exception:
                    # si autre erreur lors d'appel avec bot, on loggue l'erreur (mais ne passe pas automatiquement à sans-bot)
                    logging.error(f"Erreur lors de l'appel {name} avec bot :\n{traceback.format_exc()}")
                    # tenter sans bot au cas où
                    try:
                        fn()
                    except Exception:
                        logging.error(f"Erreur lors de l'appel {name} sans bot :\n{traceback.format_exc()}")

                logging.info(f"✅ {name} exécuté (tentative faite).")
                # Stocker la période même si la tâche a levé une exception afin d'éviter boucles infinies
                last_run[context_key] = period_marker
                return True
            except Exception:
                logging.error(f"Erreur fatale durant l'exécution de {name} :\n{traceback.format_exc()}")
                # stocker la tentative pour éviter retry immédiat
                if period_marker:
                    last_run[context_key] = period_marker
                return False

        try:
            # ---------------------------------------
            # 09:00 → Film + Quiz + News (AniList + RSS)
            # ---------------------------------------
            if heure == "09:00":
                key = "daily_09"
                if last_run.get(key) != _date_str():
                    logging.info("Trigger 09:00 — film / quiz / actu")
                    _call_task(publier_film, "publier_film", key)
                    _call_task(publier_quiz, "publier_quiz", key)
                    _call_task(publier_actu_privee, "publier_actu_privee", key)
                else:
                    logging.debug("09:00 déjà exécuté aujourd'hui — saut.")

            # ---------------------------------------
            # 15:00 → Correction quiz
            # ---------------------------------------
            if heure == "15:00":
                key = "daily_15"
                if last_run.get(key) != _date_str():
                    logging.info("Trigger 15:00 — correction quiz")
                    _call_task(publier_correction, "publier_correction", key)
                else:
                    logging.debug("15:00 déjà exécuté aujourd'hui — saut.")

            # ---------------------------------------
            # 18:00 → Anniversaires du jour + anecdote cinéma
            # ---------------------------------------
            if heure == "18:00":
                key = "daily_18"
                if last_run.get(key) != _date_str():
                    logging.info("Trigger 18:00 — anniversaires")
                    _call_task(publier_anniversaires, "publier_anniversaires", key)
                else:
                    logging.debug("18:00 déjà exécuté aujourd'hui — saut.")

            # ---------------------------------------
            # 21:30 → Message privé aux admins (rappel / résumé)
            # ---------------------------------------
            if heure == "21:30":
                key = "daily_21_30"
                if last_run.get(key) != _date_str():
                    logging.info("Trigger 21:30 — notifier_admins_daily")
                    _call_task(notifier_admins_daily, "notifier_admins_daily", key)
                else:
                    logging.debug("21:30 déjà exécuté aujourd'hui — saut.")

            # ---------------------------------------
            # 20:00 dimanche → Stats + Top abonnés
            # ---------------------------------------
            if now.weekday() == 6 and heure == "20:00":
                key = "weekly_sun_20"
                if last_run.get(key) != _week_str():
                    logging.info("Trigger dimanche 20:00 — stats hebdo")
                    _call_task(envoyer_statistiques, "envoyer_statistiques", key)
                    _call_task(publier_meilleurs_abonnes, "publier_meilleurs_abonnes", key)
                else:
                    logging.debug("Weekly 20:00 déjà exécuté pour cette semaine — saut.")

            # ---------------------------------------
            # 1er jour du mois à 10:00 → Abonnés du mois
            # ---------------------------------------
            if now.day == 1 and heure == "10:00":
                key = "monthly_1_10"
                if last_run.get(key) != _month_str():
                    logging.info("Trigger 1er du mois 10:00 — abonnés du mois")
                    _call_task(publier_abonnes_du_mois, "publier_abonnes_du_mois", key)
                else:
                    logging.debug("Monthly 1er 10:00 déjà exécuté pour ce mois — saut.")

            # ---------------------------------------
            # 22:00 → Sauvegarde logique + backup
            # ---------------------------------------
            if heure == "22:00":
                key = "daily_22"
                if last_run.get(key) != _date_str():
                    logging.info("Trigger 22:00 — sauvegarde + backup")
                    _call_task(sauvegarder_donnees, "sauvegarder_donnees", key)
                    # backup_donnees peut accepter un bot ou non : on gère les deux cas
                    try:
                        backup_donnees(bot)
                    except TypeError:
                        try:
                            backup_donnees()
                        except Exception:
                            logging.error(f"Erreur backup_donnees:\n{traceback.format_exc()}")
                    except Exception:
                        logging.error(f"Erreur backup_donnees:\n{traceback.format_exc()}")
                    # enregistrer la tentative
                    last_run[key] = _date_str()
                else:
                    logging.debug("22:00 déjà exécuté aujourd'hui — saut.")

        except Exception as e:
            logging.error("❌ Erreur dans la boucle de planification :\n" + traceback.format_exc())

        # Vérification toutes les 60s (garde simple)
        sleep(60)


if __name__ == "__main__":
    # Permet d'exécuter directement le scheduler pour debug local
    try:
        lancer_taches_scheduled()
    except KeyboardInterrupt:
        logging.info("Scheduler interrompu par l'utilisateur (KeyboardInterrupt).")