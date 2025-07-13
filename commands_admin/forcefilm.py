from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['forcefilm'])
def forcefilm(message):
    bot.send_message(message.chat.id, 'Forçage du film du jour...')
