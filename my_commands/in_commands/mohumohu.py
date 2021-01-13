#mohumohu
#'もふもふ'
async def mohumohu(message):
    if message.author.bot:
        return
    await message.channel.send('もふもふ…')