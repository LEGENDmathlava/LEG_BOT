#DEBUG MyNick checkReference
async def DEBUG(m, message):
    print(message.mentions)
    if message.reference:
        message2 = await message.channel.fetch_message(message.reference.message_id)
        print(message2)
        await message.channel.send(str(message2))
    else:
        print(message)
        await message.channel.send(str(message))
async def MyNick(m, message):
    s = message.author.nick
    s = s if message.author.nick != None else message.author
    await message.channel.send(s)
async def checkReference(m, message):
    print(message.reference)
    await message.channel.send(str(message.reference))