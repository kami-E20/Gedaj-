from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['call'])
def call(message):
    bot.send_message(message.chat.id, 'Appel en attente...')
