
def register_quiz(bot):
    from telebot import types

    @bot.message_handler(commands=['quiz'])
    def send_quiz(message):
        question = "🎬 Quel film a remporté l’Oscar du Meilleur Film en 1994 ?"
        options = ["Forrest Gump", "Pulp Fiction", "The Shawshank Redemption", "Quatre mariages et un enterrement"]
        correct_option_index = 0  # Forrest Gump

        markup = types.InlineKeyboardMarkup()
        for i, option in enumerate(options):
            markup.add(types.InlineKeyboardButton(text=option, callback_data=f"quiz_{i}"))

        bot.send_message(message.chat.id, question, reply_markup=markup)
