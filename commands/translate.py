from deep_translator import GoogleTranslator
from telebot.types import Message
from loader import bot

def register_translate(dp):
    @dp.message_handler(commands=['translate'])
    def handle_translate(message: Message):
        args = message.text.split(maxsplit=2)
        if len(args) < 3:
            bot.reply_to(message, "❗ Utilisation : `/translate <fr/en> <texte>`", parse_mode="Markdown")
            return

        lang = args[1].lower()
        if lang not in ['fr', 'en']:
            bot.reply_to(message, "❗ Langue non prise en charge. Utilise `fr` ou `en`.", parse_mode="Markdown")
            return

        texte = args[2]
        try:
            translated = GoogleTranslator(source='auto', target=lang).translate(texte)
            bot.send_message(message.chat.id, f"🌐 Traduction ({lang}) :\n{translated}")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Erreur pendant la traduction : {e}")