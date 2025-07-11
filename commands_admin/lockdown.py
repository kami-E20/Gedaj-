def register_lockdown(bot):
    bot.add_command('lockdown', lambda msg: bot.send_message(msg.chat.id, "🔒 *Mode Lockdown activé* : toutes les commandes publiques sont temporairement désactivées."))
