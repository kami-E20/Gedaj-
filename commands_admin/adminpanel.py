def register_adminpanel(bot):
    bot.add_command('adminpanel', lambda msg: bot.send_message(msg.chat.id, "🛠️ *AdminPanel Gedaj*\nVoir statistiques, forcer publications, restaurer backup."))
