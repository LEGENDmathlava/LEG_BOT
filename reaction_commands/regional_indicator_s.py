#regional_indicator_s
#'🇸'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import stock
async def regional_indicator_s(reaction, user):
    print('🇸')
    if reaction.message.author.id == 671605558666592259 and reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')' and reaction.message.embeds[0].description == 'Now Playing':
        await stock(reaction.message, user)
        if reaction.message.author.permissions_in(reaction.message.channel).manage_messages:
            await reaction.message.remove_reaction('🇸', user)
