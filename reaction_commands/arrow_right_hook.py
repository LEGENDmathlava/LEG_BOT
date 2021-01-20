#arrow_right_hook
#'↪️'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import rotate_left
async def arrow_right_hook(reaction, user):
    print('↪️')
    if reaction.message.author.id == 671605558666592259 and reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')' and reaction.message.embeds[0].description == 'Now Playing':
        await rotate_left(reaction.message, user)
        if reaction.message.author.permissions_in(reaction.message.channel).manage_messages:
            await reaction.message.remove_reaction('↪️', user)
