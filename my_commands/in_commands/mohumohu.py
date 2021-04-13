#mohumohu
#'もふもふ'
import discord
async def mohumohu(message:discord.Message):
    if message.author.bot:
        return
    await message.channel.send('もふもふ…')