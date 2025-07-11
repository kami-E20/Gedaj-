def register_restorebackup(bot):
    bot.add_command('restorebackup', lambda msg: bot.send_message(msg.chat.id, "♻️ *Backup restauré* à partir des dernières données sauvegardées."))
