from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['defi'])
def defi(message):
    bot.send_message(message.chat.id, 'Défi du jour lancé 💥')
