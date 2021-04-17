import discord
import os
from random import randrange
import time
from typing import List, Union, Dict, Any, Optional, Tuple
from copy import deepcopy


class Game:
    def __init__(self) -> None:
        self.field = [*[list('x          x') for _ in range(20)], list('xxxxxxxxxxxx')]
        self.now_block = randrange(0, 7)
        self.block_position = (0, 0)
        self.block_angle = 0
        self.next_blocks = [randrange(0, 7) for _ in range(4)]
        self.stock_block = 7
        self.score = 0
    def split_block(self) -> List[List[str]]:
        split_block = list(map(lambda x: list(x), blocks[self.now_block].split('\n')))
        return block_rot(split_block, self.block_angle)
    def clone_field(self) -> List[List[str]]:
        return deepcopy(self.field)
    def view_field(self) -> List[List[str]]:
        split_block = self.split_block()
        field = self.clone_field()
        for y in range(4):
            for x in range(4):
                if 0 <= self.block_position[1] + y <= 20 and 0 <= 4 + self.block_position[0] + x <= 11:
                    back = field[self.block_position[1] + y][4 + self.block_position[0] + x]
                    forward = split_block[y][x]
                    if forward == 'o':
                        if back == ' ':
                            field[self.block_position[1] + y][4 + self.block_position[0] + x] = '@'
                        elif back == 'o':
                            field[self.block_position[1] + y][4 + self.block_position[0] + x] = 'x'
        return field
    def is_hit(self) -> bool:
        split_block = self.split_block()
        for y in range(4):
            for x in range(4):
                if 0 <= self.block_position[1] + y <= 20 and 0 <= 4 + self.block_position[0] + x <= 11:
                    back = self.field[self.block_position[1] + y][4 + self.block_position[0] + x]
                    forward = split_block[y][x]
                    if forward == 'o' and back != ' ':
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
        if self.stock_block == 7:
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
        for y in range(4):
            for x in range(4):
                if 0 <= self.block_position[1] + y <= 20 and 0 <= 4 + self.block_position[0] + x <= 11:
                    back = self.field[self.block_position[1] + y][4 + self.block_position[0] + x]
                    forward = split_block[y][x]
                    if forward != ' ' and back == ' ':
                        self.field[self.block_position[1] + y][4 + self.block_position[0] + x] = forward
                        print('ちゃくちっ')
        self.block_prepare()
    def block_prepare(self) -> None:
        self.now_block = 7
        self.initialize_position()
        self.initialize_angle()
    def next(self) -> None:
        self.now_block = self.next_blocks[0]
        self.next_blocks = [*self.next_blocks[1:], randrange(0, 7)]
        self.initialize_position()
        self.initialize_angle()
    def is_alive(self) -> bool:
        if self.is_hit():
            print('DEAD')
            return False
        return True
    def lines_clear(self) -> None:
        for y in range(20):
            is_line_full = True
            for x in range(12):
                back = self.field[y][x]
                if back == ' ':
                    is_line_full = False
                    break
            if is_line_full:
                self.score += 1000
                for z in range(y, 0, -1):
                    for x in range(12):
                        self.field[z][x] = self.field[z-1][x]
                self.field[0] = list('x          x')

now_preparing_players:Dict[int, Tuple[discord.Message, Game]]={}
blocks:List[str]=['    \n oo \n oo \n    ',
                  ' o  \n o  \n o  \n o  ',
                  '    \n o  \n oo \n o  ',
                  '    \n oo \n o  \n o  ',
                  '    \n oo \n  o \n  o ',
                  '    \n  o \n oo \n o  ',
                  '    \n o  \n oo \n  o ',
                  '    \n    \n    \n    ']
async def GAME_PREPARE(message:discord.Message)->None:
    global blocks
    game = Game()
    embed = discord.Embed(title='TETRIS('+str(message.author.id)+')', description='STAND BY')
    embed.add_field(name='Stock', value='```'+blocks[2]+'```', inline=False)
    embed.add_field(name='Game', value='```x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x Press ▶️  x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x          x\n'
                                        + 'x   @@     x\n'
                                        + 'x  @@      x\n'
                                        + 'x          x\n'
                                        + 'x        o x\n'
                                        + 'x       ooox\n'
                                        + 'xxxxxxxxxxxx\n```')
    embed.add_field(name='Next', value=''.join([f'```{emph(blocks[i])}```' for i in range(4)]))
    embed.add_field(name='Score', value=123)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed_message = await message.channel.send(embed=embed)
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
    embed = discord.Embed(title='TETRIS('+str(user.id)+')', description='Now Playing')
    embed.add_field(name='Stock', value='```'+blocks[game.stock_block]+'```', inline=False)
    embed.add_field(name='Game', value='```'+'\n'.join(map(''.join, view_field))+'```')
    embed.add_field(name='Next', value=''.join([f'```{emph(blocks[game.next_blocks[i]])}```' for i in range(4)]))
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
        await lines_clear(message, user)
        await next(message, user)
        return game.is_alive()
    return True

def emph(block:str)->str:
    return block.replace('o', '@')

def block_rot(block:List[List[str]], n: int)->List[List[str]]:
    temp = deepcopy(block)
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

async def exit_game(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    await message.delete()
    now_preparing_players.pop(user.id)

async def GAME_OVER(message:discord, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    view_field = game.view_field()
    embed = discord.Embed(title='TETRIS('+str(user.id)+')', description='GAME_OVER')
    embed.add_field(name='Stock', value='```'+blocks[game.stock_block]+'```', inline=False)
    embed.add_field(name='Game', value='```'+'\n'.join(map(''.join, view_field))+'```')
    embed.add_field(name='Next', value=''.join([f'```{emph(blocks[game.next_blocks[i]])}```' for i in range(4)]))
    embed.add_field(name='Score', value=game.score)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await message.edit(embed=embed)

async def lines_clear(message:discord.Message, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.lines_clear()
    await paint(message, user)

async def next(message:discord, user:Union[discord.Member, discord.User])->None:
    global now_preparing_players
    game = now_preparing_players[user.id][1]
    game.next()
    await paint(message, user)