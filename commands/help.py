from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Voici les commandes disponibles...')
