from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['forcenews'])
def forcenews(message):
    bot.send_message(message.chat.id, 'Forçage des news...')
