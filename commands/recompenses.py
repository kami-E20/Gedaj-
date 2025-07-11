def register_recompenses(bot):
    bot.add_command('recompenses', lambda msg: bot.send_message(msg.chat.id, "🎁 Récompenses du mois :\n1er : FanPass + Certificat + Affiche HD\n2e-5e : Affiches exclusives + rôles spéciaux"))
