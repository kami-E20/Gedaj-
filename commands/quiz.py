import json
from telebot import TeleBot
from datetime import date

QUIZ_LOG_FILE = "data/quiz_log.json"

def register_quiz(bot: TeleBot):
    @bot.message_handler(commands=["quiz"])
    def handle_quiz(message):
        user_id = str(message.from_user.id)
        today = str(date.today())

        try:
            with open(QUIZ_LOG_FILE, "r") as f:
                log = json.load(f)
        except:
            log = {}

        if log.get(today, {}).get(user_id):
            bot.reply_to(message, "❌ Tu as déjà répondu au quiz du jour. Reviens demain pour un nouveau défi !")
            return

        if today not in log:
            log[today] = {}
        log[today][user_id] = True

        with open(QUIZ_LOG_FILE, "w") as f:
            json.dump(log, f)

        bot.reply_to(message, "🎯 *Quiz du jour :*\nQuel est le réalisateur du film Inception ?\nA. Nolan\nB. Spielberg\nC. Tarantino", parse_mode="Markdown")