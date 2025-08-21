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

# --- AJOUTER DANS scripts/notify_block.py ---

from datetime import datetime
from loader import ADMINS
from scripts.anniversaires import fetch_anniversaires, format_anniv_message

def publier_anniversaires(bot, target_chat_ids=None):
    """
    Publie les anniversaires du jour à la/aux cible(s).
    Par défaut, uniquement aux administrateurs (ADMINS).
    Retourne True s'il y a eu au moins une publication, sinon False.
    """
    if target_chat_ids is None:
        target_chat_ids = ADMINS

    try:
        anniversaires = fetch_anniversaires()  # lit data/celeb_anniversaires.json et filtre sur MM-DD
    except Exception as e:
        print(f"⚠️ fetch_anniversaires a échoué: {e}")
        return False

    if not anniversaires:
        print("ℹ️ Aucun anniversaire aujourd'hui.")
        return False

    sent_any = False
    for entry in anniversaires:
        try:
            msg = format_anniv_message(entry)
        except Exception as e:
            print(f"⚠️ format_anniv_message erreur sur {entry}: {e}")
            continue

        for chat_id in target_chat_ids:
            try:
                bot.send_message(chat_id, msg, parse_mode="Markdown")
                sent_any = True
            except Exception as e:
                print(f"⚠️ Envoi anniversaire vers {chat_id} échoué: {e}")

    if sent_any:
        print("✅ Anniversaires publiés aux admins.")
    else:
        print("ℹ️ Aucun message anniversaire envoyé.")
    return sent_any