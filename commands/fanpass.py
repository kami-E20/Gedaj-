from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['fanpass'])
def fanpass(message):
    bot.send_message(message.chat.id, 'Voici votre Fan Pass 🎟️')
