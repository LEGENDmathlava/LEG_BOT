#ECHO
import discord
from typing import List
async def ECHO(m:List[str], message:discord.Message):
    if len(m) > 2:
        s = message.content[message.content.find(m[2], message.content.find(m[1])+5):]
        await message.reply(s)