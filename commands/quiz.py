from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['quiz'])
def quiz(message):
    bot.send_message(message.chat.id, 'Voici votre quiz cinéma du jour.')
