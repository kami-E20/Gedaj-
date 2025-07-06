from loader import bot
from telebot.types import Message
from googletrans import Translator
from utils.permissions import is_user_authorized

translator = Translator()

@bot.message_handler(commands=['translate'])
def register_translate(message: Message):
    if not is_user_authorized(message.from_user.id):
        return

    try:
        text = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.reply_to(message, "❗ Veuillez fournir un texte à traduire après la commande.")
        return

    lang = 'en' if message.from_user.language_code == 'fr' else 'fr'
    translated = translator.translate(text, dest=lang).text
    chat_id = message.chat.id
    bot.send_message(chat_id, f"📘 Traduction ({lang}) :\n\n{translated}")