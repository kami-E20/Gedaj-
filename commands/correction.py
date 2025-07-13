from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['correction'])
def correction(message):
    bot.send_message(message.chat.id, 'Correction en cours...')
