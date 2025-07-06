from telebot import TeleBot

def register_admin(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["admin"])
    def handle_admin(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "👑 Admins :\n— Kâmį (ID: 879386491)\n— Anthony (ID: 5618445554)")