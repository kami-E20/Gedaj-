from telebot import TeleBot

def register_restorebackup(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["restorebackup"])
    def handle_restorebackup(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "💾 Backup restauré avec succès.")