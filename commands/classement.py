from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['classement'])
def classement(message):
    bot.send_message(message.chat.id, 'Classement des fans 🔝')
