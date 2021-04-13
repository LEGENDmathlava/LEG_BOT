#SLEEP
import discord
from typing import List
async def SLEEP(m:List[str], message:discord.Message):
    print(chr(7))
    print(chr(7))
    print(chr(7))
    print(chr(7))
    await message.channel.send('おやすみ')
    print(chr(7))
    print(chr(7))
    print(chr(7))
    sys.exit()