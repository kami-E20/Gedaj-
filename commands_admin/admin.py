from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(message.chat.id, 'Panneau admin')
