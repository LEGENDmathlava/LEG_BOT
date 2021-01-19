#arrow_forward
#'▶️'

from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import GAME_START
async def arrow_forward(reaction, user):
    print('▶️')
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')' and reaction.message.embeds[0].description == 'STAND BY':
        await reaction.message.clear_reactions()
        await reaction.message.add_reaction('⬅️')
        await reaction.message.add_reaction('⬆️')
        await reaction.message.add_reaction('➡️')
        await reaction.message.add_reaction('⬇️')
        await reaction.message.add_reaction('↪️')
        await reaction.message.add_reaction('↩️')
        await reaction.message.add_reaction('🇸')
        await reaction.message.add_reaction('🗑️')
        await GAME_START(reaction.message, user)