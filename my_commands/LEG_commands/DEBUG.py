#DEBUG MyNick
async def DEBUG(m, message):
    print(message)
    await message.channel.send(str(message))
async def MyNick(m, message):
    s = message.author.nick
    s = s if message.author.nick != None else message.author
    await message.channel.send(s)