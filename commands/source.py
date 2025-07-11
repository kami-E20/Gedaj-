def register_source(bot):
    bot.add_command('source', lambda msg: bot.send_message(msg.chat.id, "📎 La source de cette information :\nhttps://example.com/source-fiable"))
