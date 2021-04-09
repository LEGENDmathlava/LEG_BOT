import discord
import os
from random import randrange
import time

now_preparing_players={}
blocks=['    \n oo \n oo \n    ', ' o  \n o  \n o  \n o  ', '    \n o  \n oo \n o  ', '    \n oo \n o  \n o  ', '    \n oo \n  o \n  o ', '    \n  o \n oo \n o  ', '    \n o  \n oo \n  o ', '    \n    \n    \n    ']
async def GAME_PREPARE(message):
    global blocks
    os.makedirs('my_commands/LEG_commands/TETRIS_GAME', exist_ok=True)
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(message.author.id)+'.txt', mode='w') as f:
        f.write('x          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nxxxxxxxxxxxx\n')
        f.write(str(randrange(0, 7))+'\n') # 種類
        f.write('0\n') # 相対y座標
        f.write('0\n') # 相対x座標
        f.write('0\n') # 角度
        f.write(str(randrange(0, 7))+'\n') # next1
        f.write(str(randrange(0, 7))+'\n') # next2
        f.write(str(randrange(0, 7))+'\n') # next3
        f.write(str(randrange(0, 7))+'\n') # next4
        f.write('7\n') # stock
        f.write('0\n') # score
    embed = discord.Embed(title='TETRIS('+str(message.author.id)+')', description='STAND BY')
    embed.add_field(name='Stock', value='```'+blocks[2]+'```', inline=False)
    embed.add_field(name='Game', value='```x          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx Press ▶️  x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx          x\nx   @@     x\nx  @@      x\nx          x\nx        o x\nx       ooox\nxxxxxxxxxxxx\n```')
    embed.add_field(name='Next', value='```'+emph(blocks[0])+'``````'+blocks[1]+'``````'+blocks[2]+'``````'+blocks[3]+'```')
    embed.add_field(name='Score', value=123)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed_message = await message.channel.send(embed=embed)
    now_preparing_players[message.author.id] = embed_message
    await embed_message.add_reaction('▶️')
    await embed_message.add_reaction('🗑️')

async def GAME_START(message, user):
    while True:    
        try:
            await paint(message, user)
            life = await auto_fall(message, user)
            if not life:
                await GAME_OVER(message, user)
                if message.author.permissions_in(message.channel).manage_messages:
                    await message.clear_reactions()
                await message.add_reaction('🗑️')
                global now_preparing_players
                now_preparing_players.pop(user.id)
                return
            for _ in range(100):
                time.sleep(0.01)
        except discord.errors.NotFound:
            return


async def paint(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o':
                    if back == ' ':
                        field[block_y + y][4 + block_x + x] = '@'
                    elif back == 'o':
                        field[block_y + y][4 + block_x + x] = 'x'
    embed = discord.Embed(title='TETRIS('+str(user.id)+')', description='Now Playing')
    embed.add_field(name='Stock', value='```'+blocks[stock]+'```', inline=False)
    embed.add_field(name='Game', value='```'+''.join(map(''.join, field))+'```')
    embed.add_field(name='Next', value='```'+emph(blocks[next1])+'``````'+blocks[next2]+'``````'+blocks[next3]+'``````'+blocks[next4]+'```')
    embed.add_field(name='Score', value=score)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await message.edit(embed=embed)

async def move_left(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    block_x -= 1
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o' and back != ' ':
                    return
    field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)

async def move_right(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    block_x += 1
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o' and back != ' ':
                    return
    field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)

async def move_down(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    block_y += 1
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o' and back != ' ':
                    return
    field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)

async def move_fall(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    b = True
    if block_type == 7:
        return
    while b:
        block_y += 1
        for y in range(4):
            for x in range(4):
                if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                    back = field[block_y + y][4 + block_x + x]
                    forward = split_block[y][x]
                    if forward == 'o' and back != ' ':
                        b = False
                        block_y -= 1
    field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)

async def rotate_right(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    block_angle = (block_angle + 1) % 4
    split_block = block_rot(split_block, block_angle)
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o' and back != ' ':
                    return
    field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)

async def rotate_left(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    block_angle = (block_angle - 1) % 4
    split_block = block_rot(split_block, block_angle)
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o' and back != ' ':
                    return
    field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)

async def stock(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    if stock == 7:
        field_write(field, next1, 0, 0, 0, next2, next3, next4, randrange(0, 7), block_type, score, user)
    else:
        field_write(field, stock, 0, 0, 0, next1, next2, next3, next4, block_type, score, user)
    await paint(message, user)

async def auto_fall(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    block_y += 1
    b = True
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11 and b:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o' and back != ' ':
                    b = False
    if b:
        field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    else:
        block_y -= 1
        for y in range(4):
            for x in range(4):
                if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                    back = field[block_y + y][4 + block_x + x]
                    forward = split_block[y][x]
                    if forward == 'o' and back == ' ':
                        field[block_y + y][4 + block_x + x] = 'o'
        field_write(field, 7, 0, 0, 0, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)
    if not b:
        await lines_clear(message, user)
        await next(message, user)
        return is_alive(user)
    return True

def emph(block:str):
    return block.replace('o', '@')

def block_rot(block, n: int):
    temp = [[None for _ in range(4)] for _ in range(4)]
    if n == 0:
        for y in range(4):
            for x in range(4):
                temp[y][x] = block[y][x]
    elif n == 1:
        for y in range(4):
            for x in range(4):
                temp[y][x] = block[3-x][y]
    elif n == 2:
        for y in range(4):
            for x in range(4):
                temp[y][x] = block[3-y][3-x]
    elif n == 3:
        for y in range(4):
            for x in range(4):
                temp[y][x] = block[x][3-y]
    return temp

def field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='w') as f:
        f.write(''.join(map(''.join, field)))
        f.write(str(block_type)+'\n')
        f.write(str(block_y)+'\n')
        f.write(str(block_x)+'\n')
        f.write(str(block_angle)+'\n')
        f.write(str(next1)+'\n')
        f.write(str(next2)+'\n')
        f.write(str(next3)+'\n')
        f.write(str(next4)+'\n')
        f.write(str(stock)+'\n')
        f.write(str(score)+'\n')

async def exit_game(message, user):
    global now_preparing_players
    await message.delete()
    now_preparing_players.pop(user.id)

def is_alive(user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o' and back != ' ':
                    return False
    return True

async def GAME_OVER(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    for y in range(4):
        for x in range(4):
            if 0 <= block_y + y <= 20 and 0 <= 4 + block_x + x <= 11:
                back = field[block_y + y][4 + block_x + x]
                forward = split_block[y][x]
                if forward == 'o':
                    if back == ' ':
                        field[block_y + y][4 + block_x + x] = '@'
                    elif back == 'o':
                        field[block_y + y][4 + block_x + x] = 'x'
    embed = discord.Embed(title='TETRIS('+str(user.id)+')', description='GAME_OVER')
    embed.add_field(name='Stock', value='```'+blocks[stock]+'```', inline=False)
    embed.add_field(name='Game', value='```'+''.join(map(''.join, field))+'```')
    embed.add_field(name='Next', value='```'+emph(blocks[next1])+'``````'+blocks[next2]+'``````'+blocks[next3]+'``````'+blocks[next4]+'```')
    embed.add_field(name='Score', value=score)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await message.edit(embed=embed)

async def lines_clear(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    for y in range(20):
        is_line_full = True
        for x in range(12):
            back = field[y][x]
            if back == ' ':
                is_line_full = False
        if is_line_full:
            score += 1000
            for z in range(y, 0, -1):
                for x in range(12):
                    field[z][x] = field[z-1][x]
            field[0] = list('x          x\n')
    field_write(field, block_type, block_y, block_x, block_angle, next1, next2, next3, next4, stock, score, user)
    await paint(message, user)

async def next(message, user):
    with open('my_commands/LEG_commands/TETRIS_GAME/TETRIS'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(21):
            field.append(list(f.readline()))
        block_type = int(f.readline())
        block_y = int(f.readline())
        block_x = int(f.readline())
        block_angle = int(f.readline())
        next1 = int(f.readline())
        next2 = int(f.readline())
        next3 = int(f.readline())
        next4 = int(f.readline())
        stock = int(f.readline())
        score = int(f.readline())
    split_block = list(map(list, blocks[block_type].split('\n')))
    split_block = block_rot(split_block, block_angle)
    field_write(field, next1, 0, 0, 0, next2, next3, next4, randrange(0, 7), stock, score, user)
    await paint(message, user)