
from telebot.types import Message
from loader import bot

def register_inviter(dp):
    @bot.message_handler(commands=["inviter"])
    def send_invite(message: Message):
        response = (
            "📩 Invite tes amis à rejoindre Geekmania !\n"
            "Voici ton lien d’invitation personnalisé :\n"
            f"https://t.me/GEEKMANIA?start={message.from_user.id}"
        )
        bot.reply_to(message, response)
