from telebot.types import Message
from deep_translator import GoogleTranslator

def register_translate(bot):
    @bot.message_handler(commands=['translate'])
    def handle_translate(message: Message):
        # Vérifier si l'utilisateur a répondu à un message sans texte supplémentaire
        if message.reply_to_message and len(message.text.strip().split()) == 1:
            text_to_translate = message.reply_to_message.text
            if not text_to_translate:
                bot.send_message(message.chat.id, "❌ Le message répondu ne contient pas de texte.")
                return
        else:
            parts = message.text.split(' ', 1)
            if len(parts) < 2 or not parts[1].strip():
                bot.send_message(
                    message.chat.id,
                    "🔄 Utilisation : `/translate Votre texte à traduire`\n"
                    "Ou répondez à un message avec `/translate`.",
                    parse_mode="Markdown"
                )
                return
            text_to_translate = parts[1]

        try:
            lang_code = message.from_user.language_code or 'fr'
            target_lang = 'fr' if lang_code.startswith('en') else 'en'
            translated = GoogleTranslator(source='auto', target=target_lang).translate(text_to_translate)
            bot.send_message(message.chat.id, f"🔤 Traduction :\n\n{translated}")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Erreur lors de la traduction : {str(e)}")