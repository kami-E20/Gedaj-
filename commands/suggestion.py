from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['suggestion'])
def suggestion(message):
    bot.send_message(message.chat.id, 'Merci pour votre suggestion !')
