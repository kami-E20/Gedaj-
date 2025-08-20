# scripts/publisher.py

from scripts.notify_block import (
    publier_actu_privee,
    publier_anniversaires,   # ✅ anniversaires quotidiens
    publier_film,
    publier_quiz,
    publier_correction,
    publier_meilleurs_abonnes,
    publier_abonnes_du_mois,
    envoyer_statistiques,
    sauvegarder_donnees,
)
from scripts.backup import backup_donnees


def run_all(bot=None):
    """
    Exécute manuellement toutes les publications et sauvegardes.
    À utiliser par un administrateur pour forcer les publications.
    Ordre:
      1) Actu privée (news)
      2) Anniversaires
      3) Film du jour
      4) Quiz du jour
      5) Correction du quiz
      6) Classements / Stats
      7) Sauvegarde + Backup
    """
    try:
        print("🚀 Lancement manuel des publications...")

        if bot:
            # 🔔 Publications principales
            try:
                print("📰 publier_actu_privee ...")
                publier_actu_privee(bot)
            except Exception as e:
                print(f"⚠️ publier_actu_privee a échoué: {e}")

            try:
                print("🎂 publier_anniversaires ...")
                publier_anniversaires(bot)
            except Exception as e:
                print(f"⚠️ publier_anniversaires a échoué: {e}")

            try:
                print("🎬 publier_film ...")
                publier_film(bot)
            except Exception as e:
                print(f"⚠️ publier_film a échoué: {e}")

            try:
                print("❓ publier_quiz ...")
                publier_quiz(bot)
            except Exception as e:
                print(f"⚠️ publier_quiz a échoué: {e}")

            try:
                print("✅ publier_correction ...")
                publier_correction(bot)
            except Exception as e:
                print(f"⚠️ publier_correction a échoué: {e}")

            # 🏆 Classements & stats
            try:
                print("🏅 publier_meilleurs_abonnes ...")
                publier_meilleurs_abonnes(bot)
            except Exception as e:
                print(f"⚠️ publier_meilleurs_abonnes a échoué: {e}")

            try:
                print("🎁 publier_abonnes_du_mois ...")
                publier_abonnes_du_mois(bot)
            except Exception as e:
                print(f"⚠️ publier_abonnes_du_mois a échoué: {e}")

            try:
                print("📊 envoyer_statistiques ...")
                envoyer_statistiques(bot)
            except Exception as e:
                print(f"⚠️ envoyer_statistiques a échoué: {e}")
        else:
            print("⚠️ Aucun bot fourni → seules les sauvegardes seront exécutées.")

        # 💾 Sauvegardes (robuste aux signatures différentes)
        try:
            print("💾 sauvegarder_donnees ...")
            try:
                # Essaye d'abord avec bot
                sauvegarder_donnees(bot)
            except TypeError:
                # Repli sans bot si la signature ne l'accepte pas
                sauvegarder_donnees()
        except Exception as e:
            print(f"⚠️ sauvegarder_donnees a échoué: {e}")

        try:
            print("🗄️ backup_donnees ...")
            backup_donnees(bot)
        except TypeError:
            try:
                backup_donnees()
            except Exception as e:
                print(f"⚠️ backup_donnees a échoué: {e}")
        except Exception as e:
            print(f"⚠️ backup_donnees a échoué: {e}")

        print("✅ run_all terminé.")
    except Exception as e:
        print(f"❌ Erreur dans run_all : {e}")