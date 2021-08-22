# ECHO_FLOWER
import discord
from typing import List


async def ECHO_FLOWER(m: List[str], message: discord.Message) -> None:
    f = open('ECHO_FLOWER')
    s = ''
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    line = f.readline()
    while line:
        line = line.replace('ECHO_FLOWER', '∎∎∎∎_∎∎∎∎∎∎')
        s += line
        line = f.readline()
    f.close()
    await message.channel.send(s)
