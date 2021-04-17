import discord
import os
from random import randrange
import time
from typing import List, Union, Tuple, Dict
from copy import deepcopy

class Game:
    def __init__(self) -> None:
        self.field = [[' ', ' ', ' ', '\n'] for _ in range(12)]
        self.now_block = (str(randrange(0, 7)), str(randrange(0, 7)))
        self.block_position = (0, 0)
        self.block_angle = 0
        self.next_blocks = [(str(randrange(0, 7)), str(randrange(0, 7))) for _ in range(6)]
        self.stock_block = (' ', ' ')
        self.score = 0
    def split_block(self) -> List[List[str]]:
        block = [[' ', ' ', ' '], [' ', self.now_block[0], ' '], [' ', ' ', ' ']]
        if self.block_angle == 0:
            block[1][2] = self.now_block[1]
        if self.block_angle == 1:
            block[2][1] = self.now_block[1]
        if self.block_angle == 2:
            block[1][0] = self.now_block[1]
        if self.block_angle == 3:
            block[0][1] = self.now_block[1]
        return block
    def clone_field(self) -> List[List[str]]:
        return deepcopy(self.field)
    def view_field(self) -> List[List[str]]:
        split_block = self.split_block()
        field = self.clone_field()
        for y in range(12):
            for x in range(3):
                if field[y][x] != ' ' and field[y][x] != 'w' and self.count_rinsetsu(x, y) >= 2:
                    whiten(field, x, y)
        for y in range(12):
            for x in range(3):
                field[y][x] = blocks[field[y][x]]
        for y in range(3):
            for x in range(3):
                if 0 <= self.block_position[1] + y - 1 <= 11 and 0 <= self.block_position[0] + x <= 2:
                    back = field[self.block_position[1] + y - 1][self.block_position[0] + x]
                    forward = split_block[y][x]
                    if forward != ' ':
                        if back == ' ':
                            field[self.block_position[1] + y - 1][self.block_position[0] + x] = blocks[forward]
                        elif back != ' ':
                            field[self.block_position[1] + y - 1][self.block_position[0] + x] = '||' + blocks[forward] + '||'
        return field
    def is_hit(self) -> bool:
        split_block = self.split_block()
        for y in range(3):
            for x in range(3):
                if 0 <= self.block_position[1] + y - 1 <= 11 and 0 <= self.block_position[0] + x <= 2:
                    back = self.field[self.block_position[1] + y - 1][self.block_position[0] + x]
                else:
                    back = 'w'
                forward = split_block[y][x]
                if forward != ' ' and back != ' ':
                    print('どすっ')
                    return True
        return False
    def initialize_position(self) -> None:
        self.block_position = 0, 0
    def move_free(self, x: int, y: int) -> None:
        self.block_position = self.block_position[0] + x, self.block_position[1] + y
    def initialize_angle(self) -> None:
        self.block_angle = 0
    def rotate_free(self, n: int) -> None:
        self.block_angle = (self.block_angle + n) % 4
    def move_left(self) -> None:
        self.move_free(-1, 0)
        if self.is_hit():
            self.move_free(1, 0)
    def move_right(self) -> None:
        self.move_free(1, 0)
        if self.is_hit():
            self.move_free(-1, 0)
    def move_down(self) -> None:
        self.move_free(0, 1)
        if self.is_hit():
            self.move_free(0, -1)
    def move_fall(self) -> None:
        while True:
            self.move_free(0, 1)
            if self.is_hit():
                self.move_free(0, -1)
                return
    def rotate_right(self) -> None:
        self.rotate_free(1)
        if self.is_hit():
            self.rotate_free(-1)
    def rotate_left(self) -> None:
        self.rotate_free(-1)
        if self.is_hit():
            self.rotate_free(1)
    def stock(self) -> None:
        if self.stock_block == (' ', ' '):
            self.stock_block = self.now_block
            self.next()
        else:
            self.now_block, self.stock_block = self.stock_block, self.now_block
            self.initialize_position()
            self.initialize_angle()
    def auto_fall(self) -> bool:
        self.move_free(0, 1)
        if self.is_hit():
            self.move_free(0, -1)
            self.land()
            return True
        return False
    def land(self) -> None:
        split_block = self.split_block()
        for y in range(3):
            for x in range(3):
                if 0 <= self.block_position[1] + y - 1 <= 11 and 0 <= self.block_position[0] + x <= 2:
                    back = self.field[self.block_position[1] + y - 1][self.block_position[0] + x]
                    forward = split_block[y][x]
                    if forward != ' ' and back == ' ':
                        self.field[self.block_position[1] + y - 1][self.block_position[0] + x] = forward
                        print('ちゃくちっ')
        self.block_prepare()
    def block_prepare(self) -> None:
        self.now_block = (' ', ' ')
        self.initialize_position()
        self.initialize_angle()
    def next(self) -> None:
        self.now_block = self.next_blocks[0]
        self.next_blocks = [*self.next_blocks[1:], (str(randrange(0, 7)), str(randrange(0, 7)))]
        self.initialize_position()
        self.initialize_angle()
    def is_alive(self) -> bool:
        if self.is_hit():
            print('DEAD')
            return False
        return True
    def blocks_fall(self) -> None:
        for y in reversed(range(12)):
            for x in range(3):
                down = 1
                while True:
                    if 0 <= y + down <= 11:
                        back = self.field[y+down][x]
                    else:
                        back = 'w'
                    forward = self.field[y][x]
                    if forward == ' ' or forward != ' ' and back != ' ':
                        down -= 1
                        break
                    down += 1
                if down != 0:
                    self.field[y+down][x] = self.field[y][x]
                    self.field[y][x] = ' '
    def rensa(self, rensasuu: int) -> bool:
        flag = False
        doujikeshi = 0
        for y in range(12):
            for x in range(3):
                if self.field[y][x] != ' ' and self.field[y][x] != 'w' and self.count_rinsetsu(x, y) >= 2:
                    doujikeshi = self.block_shoukyo(x, y, 0)
                    flag = True
        self.score += (rensasuu + 1) * doujikeshi * 10
        return flag
    def count_rinsetsu(self, x:int, y:int)->int:
        n=0
        if x <= 1 and self.field[y][x+1] == self.field[y][x]:
            n += 1
        if y <= 10 and self.field[y+1][x] == self.field[y][x]:
            n += 1
        if x >= 1 and self.field[y][x-1] == self.field[y][x]:
            n += 1
        if y >= 1 and self.field[y-1][x] == self.field[y][x]:
            n += 1
        return n
    def block_shoukyo(self, x:int, y:int, doujikeshi:int)->int:
        block_type:str = self.field[y][x]
        self.field[y][x] = ' '
        n=doujikeshi
        if x <= 1 and self.field[y][x+1] == block_type:
            n = block_shoukyo(self.field, x+1, y, n)
        if y <= 10 and self.field[y+1][x] == block_type:
            n = block_shoukyo(self.field, x, y+1, n)
        if x >= 1 and self.field[y][x-1] == block_type:
            n = block_shoukyo(self.field, x-1, y, n)
        if y >= 1 and self.field[y-1][x] == block_type:
            n = block_shoukyo(self.field, x, y-1, n)
        return n+1




now_preparing_players :Dict[int, Tuple[discord.Message, Game]] ={}
blocks = {'0':'<:0_:802403190397075516>', '1':'<:1_:802403829575974952>', '2':'<:2_:802404274129862710>', '3':'<:3_:802404390689439754>', '4':'<:4_:802404465256038468>', '5':'<:5_:802404605362176042>', '6':'<:6_:802404663759994890>', 'w':'<:wh:822422328926273566>', ' ':'<:bg:802405577946300446>'}
async def GAME_PREPARE(message:discord.Message)->None:
    global blocks
    game = Game()
    embed = discord.Embed(title='TESTGAME('+str(message.author.id)+')', description='STAND BY')
    embed.add_field(name='Stock', value='<:2_:802404274129862710><:3_:802404390689439754>', inline=False)
    embed.add_field(name='Game', value='<:0_:802403190397075516><:0_:802403190397075516><:0_:802403190397075516>\n<:6_:802404663759994890><:bg:802405577946300446><:bg:802405577946300446>\n<:2_:802404274129862710><:3_:802404390689439754><:bg:802405577946300446>\n<:bg:802405577946300446><:bg:802405577946300446><:0_:802403190397075516>\n<:3_:802404390689439754><:0_:802403190397075516><:3_:802404390689439754>\n<:bg:802405577946300446><:bg:802405577946300446><:6_:802404663759994890>\n<:2_:802404274129862710><:2_:802404274129862710><:0_:802403190397075516>\n<:3_:802404390689439754><:0_:802403190397075516><:2_:802404274129862710>\n<:6_:802404663759994890><:6_:802404663759994890><:0_:802403190397075516>\n<:0_:802403190397075516><:6_:802404663759994890><:0_:802403190397075516>\n<:2_:802404274129862710><:3_:802404390689439754><:6_:802404663759994890>\n<:3_:802404390689439754><:0_:802403190397075516><:0_:802403190397075516>')
    embed.add_field(name='Next', value='<:0_:802403190397075516><:1_:802403829575974952>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:2_:802404274129862710><:3_:802404390689439754>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:4_:802404465256038468><:5_:802404605362176042>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:6_:802404663759994890><:0_:802403190397075516>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:1_:802403829575974952><:2_:802404274129862710>\n<:bg:802405577946300446><:bg:802405577946300446>\n<:3_:802404390689439754><:4_:802404465256038468>')
    embed.add_field(name='Score', value=123)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed_message:discord.Message = await message.channel.send(embed=embed)
    now_preparing_players[message.author.id] = (embed_message, game)
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
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    view_field = game.view_field()
    embed = discord.Embed(title='TESTGAME('+str(user.id)+')', description='Now Playing')
    embed.add_field(name='Stock', value=blocks[game.stock_block[0]]+blocks[game.stock_block[1]], inline=False)
    embed.add_field(name='Game', value=''.join(map(''.join, view_field)))
    embed.add_field(name='Next', value = ('\n' + blocks[' '] * 2 + '\n').join(blocks[game.next_blocks[i][0]]+blocks[game.next_blocks[i][1]] for i in range(6)))
    embed.add_field(name='Score', value=game.score)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await message.edit(embed=embed)

async def GAME_OVER(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    view_field = game.view_field()
    embed = discord.Embed(title='TESTGAME('+str(user.id)+')', description='GAME_OVER')
    embed.add_field(name='Stock', value=blocks[game.stock_block[0]]+blocks[game.stock_block[1]], inline=False)
    embed.add_field(name='Game', value='\n'.join(map(''.join, view_field)))
    embed.add_field(name='Next', value = ('\n' + blocks[' '] * 2 + '\n').join(blocks[game.next_blocks[i][0]]+blocks[game.next_blocks[i][1]] for i in range(6)))
    embed.add_field(name='Score', value=game.score)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await message.edit(embed=embed)

async def move_left(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.move_left()
    await paint(message, user)

async def move_right(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.move_right()
    await paint(message, user)

async def move_down(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.move_down()
    await paint(message, user)

async def move_fall(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.move_fall()
    await paint(message, user)

async def rotate_right(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.rotate_right()
    await paint(message, user)

async def rotate_left(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.rotate_left()
    await paint(message, user)

async def stock(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.stock()
    await paint(message, user)

async def auto_fall(message:discord.Message, user:Union[discord.Member, discord.User])->bool:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    flag = game.auto_fall()
    await paint(message, user)
    if flag:
        await blocks_fall(message, user)
        rensasuu = 0
        while flag := await rensa(message, user, rensasuu):
            await blocks_fall(message, user)
            rensasuu += 1
        await next(message, user)
        return game.is_alive()
    return True

async def next(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.next()
    await paint(message, user)


async def exit_game(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    await message.delete()
    now_preparing_players.pop(user.id)

async def blocks_fall(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.blocks_fall()
    await paint(message, user)

async def rensa(message:discord.Message, user:Union[discord.Member, discord.User], rensasuu:int)->bool:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    flag = game.rensa(rensasuu)
    await paint(message, user)
    return flag

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