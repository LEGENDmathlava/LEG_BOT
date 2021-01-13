#char_NAME RAND_CHAR n_char_NAME

import random

def setCharDict():
    f = open('my_commands/LEG_commands/characters/uni.txt')
    chardict = {}
    line = f.readline()
    while line:
        linedata = line.split(';')
        if linedata[1][-8:] == ', First>':
            linedata[1] = linedata[1][:-8] + '>'
            linedata2 = f.readline().split(';')
            for i in range(int(linedata[0], 16), int(linedata2[0], 16) + 1):
                chardict[i] = linedata
        else:
            chardict[int(linedata[0], 16)] = linedata
        line = f.readline()
    f.close()
    for i in range(1114109):
        if i not in chardict:
            chardict[i] = None
    return chardict

def setJoyoDict():
    f = open('my_commands/LEG_commands/characters/joyo.txt')
    joyodict = {}
    line = f.readline()
    while line:
        if line[0] == '#':
            line = f.readline()
            continue
        linedata = line.split('\t')
        if linedata[0] != '':
            joyodict[ord(linedata[0])] = linedata
        if linedata[1] != '':
            joyodict[ord(linedata[0])] = linedata
        line = f.readline()
    f.close()
    return joyodict

def setUniHanDict():
    f = open('my_commands/LEG_commands/characters/unihan.txt')
    unihandict = {}
    line = f.readline()
    while line:
        if line[0] != '':
            unihandict[ord(line[0])] = line
        line = f.readline()
    f.close()
    return unihandict

chardict = setCharDict()
joyodict = setJoyoDict()
unihandict = setUniHanDict()

async def char_NAME(m, message):
    if len(m) < 3:
        await message.channel.send('文字を一つ以上必要です')
    s=''
    my_str = message.content[message.content.find(m[2], message.content.find(m[1])+5):]
    for ss in my_str:
        k = ord(ss)
        if chardict[k] == None:
           s += str(None) + '\n'
           continue
        char_NAME = chardict[k][1]
        char_OLD_NAME = chardict[k][10]
        if char_OLD_NAME != '':
            char_NAME += '(' + char_OLD_NAME + ')'
        if k in joyodict:
            YOMI = joyodict[k][5].split('\n')[0]
            char_NAME+='「'+YOMI+'」'
        if k in unihandict:
            YOMI = unihandict[k][2:].split('\n')[0]
            char_NAME+='『'+YOMI+'』'
        s += char_NAME + '\n'
    await message.channel.send(s[:2000])
    
async def RAND_CHAR(m, message):
    r = random.choice(list(chardict.keys()))
    while chardict[r] == None:
        r = random.choice(list(chardict.keys()))
    char_NAME = chardict[r][1]
    char_OLD_NAME = chardict[r][10]
    if char_OLD_NAME != '':
        char_NAME += '(' + char_OLD_NAME + ')'
    if r in joyodict:
        YOMI = joyodict[r][5].split('\n')[0]
        char_NAME+='「'+YOMI+'」'
    if r in unihandict:
        YOMI = unihandict[r][2:].split('\n')[0]
        char_NAME+='『'+YOMI+'』'
    await message.channel.send(chr(r)+char_NAME)


async def n_char_NAME(m, message):
    s=''
    my_str = message.content[message.content.find(m[2], message.content.find(m[1])+5):]
    for ss in my_str:
        k = ord(ss)
        if chardict[k] == None:
           s += hex(k) + ' ' + str(None) + '\n'
           continue
        char_NAME = chardict[k][1]
        char_OLD_NAME = chardict[k][10]
        if char_OLD_NAME != '':
            char_NAME += '(' + char_OLD_NAME + ')'
        if k in joyodict:
            YOMI = joyodict[k][5].split('\n')[0]
            char_NAME+='「'+YOMI+'」'
        if k in unihandict:
            YOMI = unihandict[k][2:].split('\n')[0]
            char_NAME+='『'+YOMI+'』'
        s += hex(k) + ' ' + char_NAME + '\n'
    await message.channel.send(s[:2000])