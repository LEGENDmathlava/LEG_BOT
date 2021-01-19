#arrow_right_hook
#'↪️'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import rotate_left
async def arrow_right_hook(reaction, user):
    print('↪️')
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')':
        await rotate_left(reaction.message, user)
        await reaction.message.remove_reaction('↪️', user)
