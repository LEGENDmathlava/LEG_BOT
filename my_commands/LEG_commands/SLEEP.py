#SLEEP
import discord
from typing import List
import sys
async def SLEEP(m:List[str], message:discord.Message)->None:
    print(chr(7))
    print(chr(7))
    print(chr(7))
    print(chr(7))
    await message.channel.send('おやすみ')
    print(chr(7))
    print(chr(7))
    print(chr(7))
    sys.exit()