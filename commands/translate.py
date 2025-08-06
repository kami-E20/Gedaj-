from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from deep_translator import GoogleTranslator

# Détecter la langue d’un texte
def detect_lang(text):
    return GoogleTranslator(source='auto', target='en').detect(text)

# Traduire un texte vers une langue cible
def translate_text(text, target='en'):
    return GoogleTranslator(source='auto', target=target).translate(text)

# Créer un message avec boutons de traduction
def send_translatable_message(bot, chat_id, text, parse_mode=None):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🇫🇷 Français", callback_data="translate_fr"),
        InlineKeyboardButton("🇬🇧 English", callback_data="translate_en")
    )
    bot.send_message(chat_id, text, parse_mode=parse_mode, reply_markup=markup)

# Enregistrer le gestionnaire de callback pour les boutons
def register_translation_callbacks(bot):
    @bot.callback_query_handler(func=lambda call: call.data.startswith("translate_"))
    def handle_callback(call):
        target_lang = call.data.split("_")[1]  # 'fr' ou 'en'
        if call.message and call.message.text:
            try:
                translated = translate_text(call.message.text, target=target_lang)
                bot.send_message(call.message.chat.id, f"💬 Traduction ({target_lang.upper()}) :\n{translated}")
            except Exception:
                bot.send_message(call.message.chat.id, "❌ Échec de la traduction.")

# Enregistrer la commande /translate
def register_translate_command(bot):
    @bot.message_handler(commands=['translate'])
    def handle_translate_command(message: Message):
        text_to_translate = message.text.replace("/translate", "").strip()
        if not text_to_translate:
            bot.reply_to(message, "✍️ Envoie un texte à traduire ou réponds à un message avec 'translate'.")
            return

        try:
            lang = detect_lang(text_to_translate)
            target = 'fr' if lang == 'en' else 'en'
            translated = translate_text(text_to_translate, target=target)
            bot.reply_to(message, f"💬 Traduction ({target.upper()}) :\n{translated}")
        except Exception:
            bot.reply_to(message, "❌ Je n’ai pas pu traduire ce texte.")

# Enregistrer la détection du mot 'translate' en réponse à un message
def register_translate_reply(bot):
    @bot.message_handler(func=lambda m: m.reply_to_message and m.text.strip().lower() == "translate")
    def handle_translate_reply(message: Message):
        original = message.reply_to_message.text
        if not original:
            return

        try:
            lang = detect_lang(original)
            target = 'fr' if lang == 'en' else 'en'
            translated = translate_text(original, target=target)
            bot.reply_to(message, f"💬 Traduction ({target.upper()}) :\n{translated}")
        except Exception:
            bot.reply_to(message, "❌ Traduction impossible.")

# 🔁 Fonction principale d’enregistrement à importer
def register_translate(bot):
    register_translate_command(bot)
    register_translate_reply(bot)
    register_translation_callbacks(bot)