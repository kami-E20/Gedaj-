from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['source'])
def source(message):
    bot.send_message(message.chat.id, '📚 Source : IMDb')
