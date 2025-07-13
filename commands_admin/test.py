from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, 'Test en cours...')
