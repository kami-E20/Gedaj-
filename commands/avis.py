from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['avis'])
def avis(message):
    bot.send_message(message.chat.id, 'Donnez votre avis sur le film.')
