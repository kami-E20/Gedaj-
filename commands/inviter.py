from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['inviter'])
def inviter(message):
    bot.send_message(message.chat.id, 'Invitez vos amis ici 📩')
