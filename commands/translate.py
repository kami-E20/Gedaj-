def register_translate(bot):
    bot.add_command('translate', lambda msg: bot.send_message(msg.chat.id, "🌍 Traduction activée. Le message sélectionné sera traduit selon ta langue préférée."))
