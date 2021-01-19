#arrow_down
#'⬇️'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import move_down
async def arrow_down(reaction, user):
    print('⬇️')
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')':
        await move_down(reaction.message, user)
        await reaction.message.remove_reaction('⬇️', user)