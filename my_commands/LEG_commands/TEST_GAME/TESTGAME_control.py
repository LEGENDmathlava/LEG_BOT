import discord
import os
from random import randrange
import time
from typing import List, Union

now_preparing_players={}
blocks = {'0':'<:0_:802403190397075516>', '1':'<:1_:802403829575974952>', '2':'<:2_:802404274129862710>', '3':'<:3_:802404390689439754>', '4':'<:4_:802404465256038468>', '5':'<:5_:802404605362176042>', '6':'<:6_:802404663759994890>', 'w':'<:wh:822422328926273566>', ' ':'<:bg:802405577946300446>'}
async def GAME_PREPARE(message:discord.Message)->None:
    global blocks
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(message.author.id)+'.txt', mode='w') as f:
        f.write('   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n')
        f.write(str(randrange(0, 7))+',' + str(randrange(0, 7)) + '\n') # 種類
        f.write('0 0\n') # 相対x y座標
        f.write('0\n') # 角度
        f.write(str(randrange(0, 7))+' ' + str(randrange(0, 7)) + '\n') # next1
        f.write(str(randrange(0, 7))+' ' + str(randrange(0, 7)) + '\n') # next2
        f.write(str(randrange(0, 7))+' ' + str(randrange(0, 7)) + '\n') # next3
        f.write(str(randrange(0, 7))+' ' + str(randrange(0, 7)) + '\n') # next4
        f.write(str(randrange(0, 7))+' ' + str(randrange(0, 7)) + '\n') # next5
        f.write(str(randrange(0, 7))+' ' + str(randrange(0, 7)) + '\n') # next6
        f.write(' , \n') # stock
        f.write('0\n') # score
    embed = discord.Embed(title='TESTGAME('+str(message.author.id)+')', description='STAND BY')
    embed.add_field(name='Stock', value='<:2_:802404274129862710><:3_:802404390689439754>', inline=False)
    embed.add_field(name='Game', value='<:0_:802403190397075516><:0_:802403190397075516><:0_:802403190397075516>\n<:6_:802404663759994890><:bg:802405577946300446><:bg:802405577946300446>\n<:2_:802404274129862710><:3_:802404390689439754><:bg:802405577946300446>\n<:bg:802405577946300446><:bg:802405577946300446><:0_:802403190397075516>\n<:3_:802404390689439754><:0_:802403190397075516><:3_:802404390689439754>\n<:bg:802405577946300446><:bg:802405577946300446><:6_:802404663759994890>\n<:2_:802404274129862710><:2_:802404274129862710><:0_:802403190397075516>\n<:3_:802404390689439754><:0_:802403190397075516><:2_:802404274129862710>\n<:6_:802404663759994890><:6_:802404663759994890><:0_:802403190397075516>\n<:0_:802403190397075516><:6_:802404663759994890><:0_:802403190397075516>\n<:2_:802404274129862710><:3_:802404390689439754><:6_:802404663759994890>\n<:3_:802404390689439754><:0_:802403190397075516><:0_:802403190397075516>')
    embed.add_field(name='Next', value='<:0_:802403190397075516><:1_:802403829575974952>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:2_:802404274129862710><:3_:802404390689439754>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:4_:802404465256038468><:5_:802404605362176042>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:6_:802404663759994890><:0_:802403190397075516>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:1_:802403829575974952><:2_:802404274129862710>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:3_:802404390689439754><:4_:802404465256038468>')
    embed.add_field(name='Score', value=123)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed_message:discord.Message = await message.channel.send(embed=embed)
    now_preparing_players[message.author.id] = embed_message
    await embed_message.add_reaction('▶️')
    await embed_message.add_reaction('🗑️')

async def GAME_START(message:discord.Message, user:Union[discord.Member, discord.User])->None:
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

async def paint(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    view_field = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
    for y in range(12):
        for x in range(3):
            view_field[y][x] = field[y][x]
    for y in range(12):
        for x in range(3):
            if view_field[y][x] != ' ' and view_field[y][x] != 'w' and count_rinsetsu(view_field, x, y) >= 2:
                whiten(view_field, x, y)
    for y in range(12):
        for x in range(3):
            view_field[y][x] = blocks[view_field[y][x]]
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
                forward = split_block[y][x]
                if forward != ' ':
                    if back == ' ':
                        view_field[block_y + y - 1][block_x + x] = blocks[forward]
                    elif back != ' ':
                        view_field[block_y + y - 1][block_x + x] = '||' + blocks[forward] + '||'
    embed = discord.Embed(title='TESTGAME('+str(user.id)+')', description='Now Playing')
    embed.add_field(name='Stock', value=blocks[stock1]+blocks[stock2], inline=False)
    embed.add_field(name='Game', value='\n'.join(map(''.join, view_field)))
    embed.add_field(name='Next', value=blocks[next1_1]+blocks[next1_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next2_1]+blocks[next2_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next3_1]+blocks[next3_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next4_1]+blocks[next4_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next5_1]+blocks[next5_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next6_1]+blocks[next6_2])
    embed.add_field(name='Score', value=score)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await message.edit(embed=embed)

async def GAME_OVER(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    view_field = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
    for y in range(12):
        for x in range(3):
            view_field[y][x] = field[y][x]
    for y in range(12):
        for x in range(3):
            if view_field[y][x] != ' ' and view_field[y][x] != 'w' and count_rinsetsu(view_field, x, y) >= 2:
                whiten(view_field, x, y)
    for y in range(12):
        for x in range(3):
            view_field[y][x] = blocks[field[y][x]]
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
                forward = split_block[y][x]
                if forward != ' ':
                    if back == ' ':
                        view_field[block_y + y - 1][block_x + x] = blocks[forward]
                    elif back != ' ':
                        view_field[block_y + y - 1][block_x + x] = '||' + blocks[forward] + '||'
    embed = discord.Embed(title='TESTGAME('+str(user.id)+')', description='GAME_OVER')
    embed.add_field(name='Stock', value=blocks[stock1]+blocks[stock2], inline=False)
    embed.add_field(name='Game', value='\n'.join(map(''.join, view_field)))
    embed.add_field(name='Next', value=blocks[next1_1]+blocks[next1_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next2_1]+blocks[next2_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next3_1]+blocks[next3_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next4_1]+blocks[next4_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next5_1]+blocks[next5_2]+'\n'+blocks[' ']+blocks[' ']+'\n'+blocks[next6_1]+blocks[next6_2])
    embed.add_field(name='Score', value=score)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await message.edit(embed=embed)

async def move_left(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    block_x -= 1
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
            else:
                back = 'w'
            forward = split_block[y][x]
            if forward != ' ' and back != ' ':
                print('どす')
                return
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)

async def move_right(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    block_x += 1
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
            else:
                back = 'w'
            forward = split_block[y][x]
            if forward != ' ' and back != ' ':
                return
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)

async def move_down(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    block_y += 1
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
            else:
                back = 'w'
            forward = split_block[y][x]
            if forward != ' ' and back != ' ':
                return
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)

async def move_fall(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    if block_type1 == ' ' and block_type2 == ' ':
        return
    b = True
    while b:
        block_y += 1
        for y in range(3):
            for x in range(3):
                if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                    back = field[block_y + y - 1][block_x + x]
                else:
                    back = 'w'
                forward = split_block[y][x]
                if forward != ' ' and back != ' ':
                    b = False
                    block_y -= 1
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)

async def rotate_right(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    block_angle = (block_angle + 1) % 4
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
            else:
                back = 'w'
            forward = split_block[y][x]
            if forward != ' ' and back != ' ':
                return
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)

async def rotate_left(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    block_angle = (block_angle - 1) % 4
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
            else:
                back = 'w'
            forward = split_block[y][x]
            if forward != ' ' and back != ' ':
                return
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)

async def stock(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    if stock1 == ' ' and stock2 == ' ':
        field_write(field, str(randrange(0, 7)), str(randrange(0, 7)), 0, 0, 0, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, block_type1, block_type2, score, user)
    else:
        field_write(field, stock1, stock2, 0, 0, 0, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, block_type1, block_type2, score, user)
    await paint(message, user)

async def auto_fall(message:discord.Message, user:Union[discord.Member, discord.User])->bool:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    block_y += 1
    b = True
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
            else:
                back = 'w'
            forward = split_block[y][x]
            if forward != ' ' and back != ' ':
                b = False
    if b:
        field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    else:
        block_y -= 1
        for y in range(3):
            for x in range(3):
                if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                    back = field[block_y + y - 1][block_x + x]
                    forward = split_block[y][x]
                    if forward != ' ' and back == ' ':
                        field[block_y + y - 1][block_x + x] = forward
        field_write(field, ' ', ' ', 0, 0, 0, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)
    if not b:
        await blocks_fall(message, user)
        rensasuu = 0
        while flag := await rensa(message, user, rensasuu):
            await blocks_fall(message, user)
            rensasuu += 1
        await next(message, user)
        return is_alive(user)
    return True

async def next(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    field_write(field, next1_1, next1_2, 0, 0, 0, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, str(randrange(0, 7)), str(randrange(0, 7)), stock1, stock2, score, user)
    await paint(message, user)

def is_alive(user:Union[discord.Member, discord.User])->bool:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    split_block = [[' ', ' ', ' '], [' ', block_type1, ' '], [' ', ' ', ' ']]
    if block_angle == 0:
        split_block[1][2] = block_type2
    if block_angle == 1:
        split_block[2][1] = block_type2
    if block_angle == 2:
        split_block[1][0] = block_type2
    if block_angle == 3:
        split_block[0][1] = block_type2
    for y in range(3):
        for x in range(3):
            if 0 <= block_y + y - 1 <= 11 and 0 <= block_x + x <= 2:
                back = field[block_y + y - 1][block_x + x]
            else:
                back = 'w'
            forward = split_block[y][x]
            if forward != ' ' and back != ' ':
                print('DEAD', forward, back, block_x , x, block_y, y)
                return False
    return True

def field_write(field:List[List[str]], block_type1:str, block_type2:str, block_y:int, block_x:int, block_angle:int, next1_1:str, next1_2:str, next2_1:str, next2_2:str, next3_1:str, next3_2:str, next4_1:str, next4_2:str, next5_1:str, next5_2:str, next6_1:str, next6_2:str, stock1:str, stock2:str, score:int, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='w') as f:
        f.write(''.join(map(''.join, field)))
        f.write(block_type1+','+block_type2+'\n')
        f.write(str(block_x)+' '+str(block_y)+'\n')
        f.write(str(block_angle)+'\n')
        f.write(next1_1+' '+next1_2+'\n')
        f.write(next2_1+' '+next2_2+'\n')
        f.write(next3_1+' '+next3_2+'\n')
        f.write(next4_1+' '+next4_2+'\n')
        f.write(next5_1+' '+next5_2+'\n')
        f.write(next6_1+' '+next6_2+'\n')
        f.write(stock1+','+stock2+'\n')
        f.write(str(score)+'\n')

async def exit_game(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    await message.delete()
    now_preparing_players.pop(user.id)

async def blocks_fall(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    for y in reversed(range(12)):
        for x in range(3):
            down = 1
            while True:
                if 0 <= y + down <= 11:
                    back = field[y+down][x]
                else:
                    back = 'w'
                forward = field[y][x]
                if forward == ' ' or forward != ' ' and back != ' ':
                    down -= 1
                    break
                down += 1
            if down != 0:
                field[y+down][x] = field[y][x]
                field[y][x] = ' '
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)
    await paint(message, user)

async def rensa(message:discord.Message, user:Union[discord.Member, discord.User], rensasuu:int)->bool:
    with open('my_commands/LEG_commands/TEST_GAME/TESTGAME'+str(user.id)+'.txt', mode='r') as f:
        field = []
        for _ in range(12):
            field.append(list(f.readline()))
        block_type1, block_type2 = f.readline().rstrip('\n').split(',')
        block_x, block_y = map(int, f.readline().split())
        block_angle = int(f.readline())
        next1_1, next1_2 = f.readline().split()
        next2_1, next2_2 = f.readline().split()
        next3_1, next3_2 = f.readline().split()
        next4_1, next4_2 = f.readline().split()
        next5_1, next5_2 = f.readline().split()
        next6_1, next6_2 = f.readline().split()
        stock1, stock2 = f.readline().rstrip('\n').split(',')
        score = int(f.readline())
    cleared_field=[]
    for y in range(12):
        temp = []
        for x in range(3):
            temp.append(field[y][x])
        cleared_field.append(temp)
    b = False
    doujikeshi = 0
    for y in range(12):
        for x in range(3):
            cleared_field[y][x] = field[y][x]
    for y in range(12):
        for x in range(3):
            if cleared_field[y][x] != ' ' and cleared_field[y][x] != 'w' and count_rinsetsu(cleared_field, x, y) >= 2:
                doujikeshi = block_shoukyo(cleared_field, x, y, 0)
                b = True
    for y in range(12):
        for x in range(3):
            field[y][x] = cleared_field[y][x]
    rensasuu += 1
    score += rensasuu * doujikeshi * 10
    field_write(field, block_type1, block_type2, block_y, block_x, block_angle, next1_1, next1_2, next2_1, next2_2, next3_1, next3_2, next4_1, next4_2, next5_1, next5_2, next6_1, next6_2, stock1, stock2, score, user)    
    await paint(message, user)
    return b
def count_rinsetsu(field:List[List[str]], x:int, y:int)->int:
    n=0
    if x <= 1 and field[y][x+1] == field[y][x]:
        n += 1
    if y <= 10 and field[y+1][x] == field[y][x]:
        n += 1
    if x >= 1 and field[y][x-1] == field[y][x]:
        n += 1
    if y >= 1 and field[y-1][x] == field[y][x]:
        n += 1
    return n

def whiten(view_field:List[List[str]], x:int, y:int)->None:
    block_type = view_field[y][x]
    view_field[y][x] = 'w'
    if x <= 1 and view_field[y][x+1] == block_type:
        whiten(view_field, x+1, y)
    if y <= 10 and view_field[y+1][x] == block_type:
        whiten(view_field, x, y+1)
    if x >= 1 and view_field[y][x-1] == block_type:
        whiten(view_field, x-1, y)
    if y >= 1 and view_field[y-1][x] == block_type:
        whiten(view_field, x, y-1)
    
def block_shoukyo(cleared_field:List[List[str]], x:int, y:int, doujikeshi:int)->int:
    block_type:str = cleared_field[y][x]
    cleared_field[y][x] = ' '
    n=doujikeshi
    if x <= 1 and cleared_field[y][x+1] == block_type:
        n = block_shoukyo(cleared_field, x+1, y, n)
    if y <= 10 and cleared_field[y+1][x] == block_type:
        n = block_shoukyo(cleared_field, x, y+1, n)
    if x >= 1 and cleared_field[y][x-1] == block_type:
        n = block_shoukyo(cleared_field, x-1, y, n)
    if y >= 1 and cleared_field[y-1][x] == block_type:
        n = block_shoukyo(cleared_field, x, y-1, n)
    return n+1