# scripts/publisher.py

from .notify_block import (
    publier_film,
    publier_quiz,
    publier_correction,
    publier_actu_privee,
    envoyer_statistiques,
    sauvegarder_donnees,
    publier_meilleurs_abonnes,
    publier_abonnes_du_mois,
)
from scripts.backup import backup_donnees


def run_all(bot):
    """
    Exécute manuellement toutes les publications et sauvegardes.
    Utilisable par un administrateur pour forcer les publications.
    """
    try:
        print("🚀 Lancement manuel des publications...")

        # 🔒 Publications principales
        publier_actu_privee(bot)
        publier_film(bot)
        publier_quiz(bot)
        publier_correction(bot)

        # 🏆 Classements & stats
        publier_meilleurs_abonnes(bot)
        publier_abonnes_du_mois(bot)
        envoyer_statistiques(bot)

        # 💾 Sauvegardes
        sauvegarder_donnees(bot)
        backup_donnees(bot)

        print("✅ Toutes les publications ont été exécutées avec succès.")
    except Exception as e:
        print("❌ Erreur dans run_all :", e)