from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['lang'])
def lang(message):
    bot.send_message(message.chat.id, 'Choisissez votre langue.')
