from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Bienvenue sur Gedaj !')
