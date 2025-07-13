from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['forcequiz'])
def forcequiz(message):
    bot.send_message(message.chat.id, 'Forçage du quiz du jour...')
