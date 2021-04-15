#TESTGAME
import discord
from typing import List
from my_commands.LEG_commands.TEST_GAME.TESTGAME_control import GAME_PREPARE, exit_game

async def TESTGAME(m:List[str], message:discord.Message)->None:
    from my_commands.LEG_commands.TEST_GAME.TESTGAME_control import now_preparing_players
    if len(m) == 3 and (m[2] == 'EXIT' or m[2] == 'RESET') and message.author.id in now_preparing_players:
        await exit_game(now_preparing_players[message.author.id], message.author)
        if m[2] == 'EXIT':
            return
    if message.author.id in now_preparing_players:
        await message.channel.send('Now Playing!!')
        return
    await GAME_PREPARE(message)
    