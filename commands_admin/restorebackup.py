from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['restorebackup'])
def restorebackup(message):
    bot.send_message(message.chat.id, 'Restauration en cours...')
