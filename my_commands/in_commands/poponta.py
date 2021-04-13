#poponta
#chr(129300)
import discord
async def poponta(message:discord.Message):
    if message.author.bot:
        return
    await message.channel.send(chr(129300))