from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['vision'])
def vision(message):
    bot.send_message(message.chat.id, 'Partage ta vision du film.')
