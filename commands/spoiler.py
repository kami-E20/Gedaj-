import telebot

def register_spoiler(bot):
    @bot.message_handler(commands=['spoiler'])
    def handle_spoiler(message):
        msg = bot.send_message(message.chat.id, "😶 Envoie maintenant le texte à masquer comme spoiler :")
        bot.register_next_step_handler(msg, process_spoiler)

    def process_spoiler(message):
        text = message.text.replace(".", "\\.").replace("-", "\\-").replace("!", "\\!")  # protéger MarkdownV2
        spoiler_text = f"||{text}||"
        bot.send_message(message.chat.id, f"🤫 Spoiler masqué :\n{spoiler_text}", parse_mode="MarkdownV2")