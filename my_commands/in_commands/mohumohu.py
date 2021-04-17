# mohumohu
# 'もふもふ'
import discord


async def mohumohu(message: discord.Message) -> None:
    if message.author.bot:
        return
    await message.channel.send('もふもふ…')
