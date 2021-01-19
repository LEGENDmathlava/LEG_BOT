#TETRIS
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import GAME_PREPARE
now_playing_players=set()
async def TETRIS(m, message):
    global now_playing_players
    if message.author.id in now_playing_players:
        await message.channel.send('Now Playing!!')
        return
    now_playing_players.add(message.author.id)
    await GAME_PREPARE(message)
    