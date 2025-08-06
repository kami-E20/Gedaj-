from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from deep_translator import GoogleTranslator

def translate_text(text, target='en'):
    return GoogleTranslator(source='auto', target=target).translate(text)

def register_translate_command(bot):
    @bot.message_handler(commands=['translate'])
    def handle_translate_command(message: Message):
        text_to_translate = message.text.replace("/translate", "").strip()
        if not text_to_translate:
            bot.reply_to(message, "✍️ Envoie un texte à traduire ou réponds à un message avec 'translate'.")
            return
        try:
            translated_fr = GoogleTranslator(source='auto', target='fr').translate(text_to_translate)
            translated_en = GoogleTranslator(source='auto', target='en').translate(text_to_translate)
            bot.reply_to(message, f"🇫🇷 *Français*:\n{translated_fr}\n\n🇬🇧 *English*:\n{translated_en}", parse_mode="Markdown")
        except Exception:
            bot.reply_to(message, "❌ Je n’ai pas pu traduire ce texte.")

def register_translate_reply(bot):
    @bot.message_handler(func=lambda m: m.reply_to_message and m.text.strip().lower() == "translate")
    def handle_translate_reply(message: Message):
        original = message.reply_to_message.text
        if not original:
            return
        try:
            translated_fr = GoogleTranslator(source='auto', target='fr').translate(original)
            translated_en = GoogleTranslator(source='auto', target='en').translate(original)
            bot.reply_to(message, f"🇫🇷 *Français*:\n{translated_fr}\n\n🇬🇧 *English*:\n{translated_en}", parse_mode="Markdown")
        except Exception:
            bot.reply_to(message, "❌ Traduction impossible.")

def register_translation_callbacks(bot):
    @bot.callback_query_handler(func=lambda call: call.data.startswith("translate_"))
    def handle_callback(call):
        target_lang = call.data.split("_")[1]
        try:
            translated = translate_text(call.message.text, target=target_lang)
            bot.send_message(call.message.chat.id, f"💬 Traduction ({target_lang.upper()}) :\n{translated}")
        except Exception:
            bot.send_message(call.message.chat.id, "❌ Échec de la traduction.")

def register_translate(bot):
    register_translate_command(bot)
    register_translate_reply(bot)
    register_translation_callbacks(bot)