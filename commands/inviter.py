from telebot.types import Message
from loader import bot

def register_inviter():
    @bot.message_handler(commands=['inviter'])
    def inviter(message: Message):
        text = "📩 Invite tes amis à rejoindre Geekmania !\nVoici ton lien : https://t.me/GEEKMANIA"
        bot.reply_to(message, text)
