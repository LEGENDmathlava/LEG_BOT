#DEBUG MyNick checkReference
import discord
from typing import List
async def DEBUG(m:List[str], message:discord.Message)->None:
    print(message.mentions)
    if message.reference:
        message2 = await message.channel.fetch_message(message.reference.message_id)
        print(message2)
        await message.channel.send(str(message2))
    else:
        print(message)
        await message.channel.send(str(message))
async def MyNick(m:List[str], message:discord.Message)->None:
    s:str = message.author.nick
    s = s if message.author.nick != None else message.author
    await message.channel.send(s)
async def checkReference(m:List[str], message:discord.Message)->None:
    print(message.reference)
    await message.channel.send(str(message.reference))