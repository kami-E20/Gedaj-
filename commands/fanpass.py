def register_fanpass(bot):
    bot.add_command('fanpass', lambda msg: bot.send_message(msg.chat.id, "🧢 Le *Fan Pass* est un rôle spécial réservé aux abonnés les plus actifs.\nContinue d’interagir pour le débloquer !"))
