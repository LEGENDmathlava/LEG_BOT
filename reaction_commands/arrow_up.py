#arrow_up
#'⬆️'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import move_fall
async def arrow_up(reaction, user):
    print('⬆️')
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')':
        await move_fall(reaction.message, user)
        await reaction.message.remove_reaction('⬆️', user)