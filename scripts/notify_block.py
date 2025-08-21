def publier_film(bot):
    print("🎬 Film du jour publié")

def publier_quiz(bot):
    print("❓ Quiz du jour publié")

def publier_correction(bot):
    print("✅ Correction du quiz envoyée")

def publier_actu_privee(bot):
    print("🔔 Actu privée envoyée")

def envoyer_statistiques(bot):
    print("📊 Statistiques hebdomadaires envoyées")

def sauvegarder_donnees(bot):
    print("💾 Données sauvegardées")

def publier_meilleurs_abonnes(bot):
    print("🏅 Meilleurs abonnés publiés")

def publier_abonnes_du_mois(bot):
    print("🎁 Récompenses du mois envoyées")

from commands_admin.anniversaire import envoyer_anniversaires

def run_notifications(bot):
    """
    Ce script exécute automatiquement les envois programmés :
    - Anniversaires aux admins
    - (plus tard on pourra ajouter actualités, sorties, etc.)
    """

    # Envoi automatique des anniversaires du jour
    envoyer_anniversaires(bot)

    # Ici tu pourras rajouter d’autres appels (actus, sorties, etc.)
    # ex: envoyer_actualites(bot)
    # ex: envoyer_sorties(bot)