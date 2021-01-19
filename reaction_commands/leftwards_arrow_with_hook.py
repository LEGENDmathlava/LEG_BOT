#leftwards_arrow_with_hook
#'↩️'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import rotate_right
async def leftwards_arrow_with_hook(reaction, user):
    print('↩️')
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')' and reaction.message.embeds[0].description == 'Now Playing':
        await rotate_right(reaction.message, user)
        await reaction.message.remove_reaction('↩️', user)
