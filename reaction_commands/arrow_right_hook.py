#arrow_right_hook
#'↪️'
import discord
from typing import Union
import my_commands.LEG_commands.TETRIS_GAME.TETRIS_control as TETRIS
import my_commands.LEG_commands.TEST_GAME.TESTGAME_control as TESTGAME
async def arrow_right_hook(reaction:discord.Reaction, user:Union[discord.Member, discord.User])->None:
    print('↪️')
    if reaction.message.author.id == 671605558666592259 and reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')' and reaction.message.embeds[0].description == 'Now Playing':
        await TETRIS.rotate_left(reaction.message, user)
        if reaction.message.author.permissions_in(reaction.message.channel).manage_messages:
            await reaction.message.remove_reaction('↪️', user)
    if reaction.message.author.id == 671605558666592259 and reaction.message.embeds and reaction.message.embeds[0].title == 'TESTGAME('+str(user.id)+')' and reaction.message.embeds[0].description == 'Now Playing':
        await TESTGAME.rotate_left(reaction.message, user)
        if reaction.message.author.permissions_in(reaction.message.channel).manage_messages:
            await reaction.message.remove_reaction('↪️', user)
