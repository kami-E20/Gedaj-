from .notify_block import (
    publier_film,
    publier_quiz,
    publier_correction,
    publier_actu_privee,
    envoyer_statistiques,
    sauvegarder_donnees,
    publier_meilleurs_abonnes,
    publier_abonnes_du_mois
)

def run_all(bot):
    publier_actu_privee(bot)
    publier_film(bot)
    publier_quiz(bot)
    publier_correction(bot)
    publier_meilleurs_abonnes(bot)
    publier_abonnes_du_mois(bot)
    envoyer_statistiques(bot)
    sauvegarder_donnees(bot)