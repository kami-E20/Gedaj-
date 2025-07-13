from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['translate'])
def translate(message):
    bot.send_message(message.chat.id, 'Traduction...')
