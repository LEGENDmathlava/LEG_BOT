#DEUTSCH
import random
def setDEUTSCH():
    f = open('my_commands/LEG_commands/DEUTSCH/DEUTSCH.txt')
    linelist = []
    line = f.readline()
    while line:
        linelist.append(line)
        line = f.readline()
    f.close()
    return linelist
linelist = setDEUTSCH()
async def DEUTSCH(m, message):
    await message.channel.send(random.choice(linelist))