#ECHO_FLOWER
async def ECHO_FLOWER(m, message):
    f = open('ECHO_FLOWER')
    s=''
    line = f.readline()
    while line:
        line = line.replace('ECHO_FLOWER', '∎∎∎∎_∎∎∎∎∎∎')
        s += line
        line = f.readline()
    f.close()
    await message.channel.send(s)