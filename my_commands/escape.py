#escape
async def escape(m, message):
    if message.reference:
        message2 = await message.channel.fetch_message(message.reference.message_id)
        s = message2.content
        escape_string = ''
        for ch in s:
            if ch.isascii() and not ch.isalnum() and ch != ' ' and ch != '\n':
                escape_string += '\\'
            escape_string += ch
        if len(escape_string) <= 2000:
            await message.channel.send(escape_string)
        else:
            await message.channel.send(escape_string[:2000])