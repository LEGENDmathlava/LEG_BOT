import discord
from legbot_LEG import *

async def legbot_command(message):
    i
    if message.author.bot:
        return
    mm = message.content
    m = mm.split()
    if ('Hey' in m) & ('Siri' in m):
        await message.channel.send('コマンドは特に用意してません')