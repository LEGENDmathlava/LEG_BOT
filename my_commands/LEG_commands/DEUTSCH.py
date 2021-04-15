#DEUTSCH
import discord
import random
from typing import List
def setDEUTSCH()->List[str]:
    f = open('my_commands/LEG_commands/DEUTSCH/DEUTSCH.txt')
    linelist = []
    line = f.readline()
    while line:
        linelist.append(line)
        line = f.readline()
    f.close()
    return linelist
linelist = setDEUTSCH()
async def DEUTSCH(m:List[str], message:discord.Message)->None:
    await message.channel.send(random.choice(linelist))