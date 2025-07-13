from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['recompenses'])
def recompenses(message):
    bot.send_message(message.chat.id, 'Récompenses débloquées 🏆')
