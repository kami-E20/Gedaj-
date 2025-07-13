from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['senddebug'])
def senddebug(message):
    bot.send_message(message.chat.id, 'Logs envoyés.')
