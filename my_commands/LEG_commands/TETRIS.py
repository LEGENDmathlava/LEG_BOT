#TETRIS
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import GAME_PREPARE, exit_game

async def TETRIS(m, message):
    from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import now_preparing_players
    if len(m) == 3 and (m[2] == 'EXIT' or m[2] == 'RESET') and message.author.id in now_preparing_players:
        await exit_game(now_preparing_players[message.author.id], message.author)
        if m[2] == 'EXIT':
            return
    if message.author.id in now_preparing_players:
        await message.channel.send('Now Playing!!')
        return
    await GAME_PREPARE(message)
    