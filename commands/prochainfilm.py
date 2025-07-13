from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['prochainfilm'])
def prochainfilm(message):
    bot.send_message(message.chat.id, 'Prochain film en salle : ...')
