from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp, bot
from scripts.publisher import run_all

# Liste des admins autorisés
ADMINS = [5618445554, 879386491]  # Anthony et Kâmį

@dp.message_handler(Command("run_all"))
async def handle_run_all(message: types.Message):
    user_id = message.from_user.id
    
    if user_id not in ADMINS:
        await message.reply("❌ Désolé, cette commande est réservée aux administrateurs.")
        return

    await message.reply("⚡ Lancement manuel de toutes les tâches en cours...")

    try:
        # Exécute toutes les fonctions prévues
        run_all(bot)

        # Confirmation dans le chat où la commande a été lancée
        await message.reply("✅ Toutes les publications, stats et sauvegardes ont été exécutées avec succès.")

        # Notification privée aux deux admins
        for admin_id in ADMINS:
            try:
                await bot.send_message(
                    admin_id,
                    f"🔔 La commande /run_all a été exécutée par **{message.from_user.full_name}**."
                )
            except Exception as e:
                print(f"Impossible d'envoyer une notif à {admin_id} : {e}")

    except Exception as e:
        await message.reply(f"❌ Une erreur est survenue : {e}")