from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_lang(bot):
    @bot.message_handler(commands=['lang'])
    def handle_lang(message):
        markup = InlineKeyboardMarkup()
        markup.row(
            InlineKeyboardButton("🇫🇷 Français", callback_data="set_lang_fr"),
            InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en")
        )
        bot.send_message(
            message.chat.id,
            "🌐 *Choisissez votre langue préférée :*",
            reply_markup=markup,
            parse_mode="Markdown"
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("set_lang_"))
    def callback_set_lang(call):
        lang_code = call.data.split("_")[-1]
        if lang_code == "fr":
            bot.answer_callback_query(call.id, "Langue définie sur 🇫🇷 Français.")
        elif lang_code == "en":
            bot.answer_callback_query(call.id, "Language set to 🇬🇧 English.")
        else:
            bot.answer_callback_query(call.id, "Langue non reconnue.")