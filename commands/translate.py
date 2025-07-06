from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from googletrans import Translator

translator = Translator()

def register_translate(bot):
    @bot.message_handler(commands=['translate'])
    def handle_translate(message):
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("🇬🇧 English", callback_data="translate_en"),
            InlineKeyboardButton("🇫🇷 Français", callback_data="translate_fr")
        )
        bot.reply_to(message, "🌐 Choisis la langue de traduction :", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data.startswith("translate_"))
    def handle_translation(call):
        lang = call.data.split("_")[1]
        chat_id = call.message.chat.id
        try:
            msg_to_translate = call.message.reply_to_message.text if call.message.reply_to_message else None
            if not msg_to_translate:
                bot.send_message(chat_id, "❌ Réponds à un message que tu veux traduire.")
                return
            result = translator.translate(msg_to_translate, dest=lang)
            bot.send_message(chat_id, f"🈯 Traduction ({lang}) :
{result.text}")
        except Exception:
            bot.send_message(chat_id, "⚠️ Erreur lors de la traduction.")