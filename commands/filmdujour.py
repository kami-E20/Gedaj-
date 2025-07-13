from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['filmdujour'])
def filmdujour(message):
    bot.send_message(message.chat.id, 'Film du jour : ...')
