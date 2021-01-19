#arrow_right
#'➡️'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import move_right
async def arrow_right(reaction, user):
    print('➡️')
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')':
        await move_right(reaction.message, user)
        await reaction.message.remove_reaction('➡️', user)