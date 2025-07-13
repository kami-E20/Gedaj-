from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['adminpanel'])
def adminpanel(message):
    bot.send_message(message.chat.id, 'Panel admin 📊')
