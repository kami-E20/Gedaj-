import json
from datetime import datetime
from scripts.points import ajouter_points

def register_quiz(bot):
    @bot.message_handler(commands=['quiz'])
    def handle_quiz(message):
        day = datetime.now().day
        with open(f"data/quiz/{day:02}.json", "r") as f:
            quiz = json.load(f)
        question = quiz['question']
        options = quiz['options']
        markup = types.InlineKeyboardMarkup()
        for i, opt in enumerate(options):
            markup.add(types.InlineKeyboardButton(text=opt, callback_data=f"quiz_{i}"))
        bot.send_message(message.chat.id, f"🎯 {question}", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data.startswith("quiz_"))
    def handle_quiz_answer(call):
        user_id = call.from_user.id
        selected = int(call.data.split("_")[1])
        day = datetime.now().day
        with open(f"data/quiz/{day:02}.json", "r") as f:
            quiz = json.load(f)
        if selected == quiz["reponse"]:
            bot.answer_callback_query(call.id, "Bonne réponse ! 🎉 Tu gagnes 5 points.")
            ajouter_points(user_id, "quiz_correct")
        else:
            bot.answer_callback_query(call.id, "Mauvaise réponse 😅 Pas de points.")