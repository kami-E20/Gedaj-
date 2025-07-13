from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['abodumois'])
def abodumois(message):
    bot.send_message(message.chat.id, 'Abonné du mois : ...')
