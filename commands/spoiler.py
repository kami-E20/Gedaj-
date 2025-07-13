from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['spoiler'])
def spoiler(message):
    bot.send_message(message.chat.id, '⚠️ Spoiler caché !')
