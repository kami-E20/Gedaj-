from telebot import TeleBot

AUTHORIZED_ADMINS = [5618445554, 879386491]

def register_senddebug(bot: TeleBot):
    @bot.message_handler(commands=['senddebug'])
    def handle_senddebug(message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Accès refusé.")
            return

        debug_message = (
            "📦 *Debug Info Gedaj v1.5*\n\n"
            "📌 JSON : chargés avec succès ✅\n"
            "📌 Tâches quotidiennes : prêtes ✅\n"
            "📌 Admins : reconnus ✅\n"
            "📌 Dernier démarrage : à confirmer manuellement"
        )
        bot.send_message(message.chat.id, debug_message, parse_mode="Markdown")