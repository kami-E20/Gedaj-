from telebot.types import Message

# Liste des ID admin autorisés
ADMIN_IDS = [5618445554, 879386491]  # Anthony et Kâmį

def register_call(bot):
    @bot.message_handler(commands=['call'])
    def handle_call(message: Message):
        if message.from_user.id in ADMIN_IDS:
            bot.send_message(message.chat.id, "📞 Appel administratif exécuté avec succès.")
        else:
            bot.send_message(message.chat.id, "⛔ Cette commande est réservée aux administrateurs.")