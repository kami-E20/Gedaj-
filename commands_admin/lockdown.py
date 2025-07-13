from telebot import TeleBot

bot = TeleBot('TOKEN')

@bot.message_handler(commands=['lockdown'])
def lockdown(message):
    bot.send_message(message.chat.id, 'Mode confinement activé 🔒')
