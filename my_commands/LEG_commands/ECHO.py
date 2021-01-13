#ECHO
async def ECHO(m, message):
    if len(m) > 2:
        s = message.content[message.content.find(m[2], message.content.find(m[1])+5):]
        await message.channel.send(s)