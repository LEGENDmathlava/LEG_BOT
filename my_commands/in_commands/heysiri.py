#heysiri
#'Hey Siri'
import discord
async def heysiri(message:discord.Message)->None:
    await message.channel.send('お呼びでしょうか')