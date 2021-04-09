#arrow_forward
#'▶️'
now_playing_players=set()
import my_commands.LEG_commands.TETRIS_GAME.TETRIS_control as TETRIS
import my_commands.LEG_commands.TEST_GAME.TESTGAME_control as TESTGAME
async def arrow_forward(reaction, user):
    print('▶️')
    if reaction.message.author.id == 671605558666592259 and reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')' and reaction.message.embeds[0].description == 'STAND BY' and user.id not in now_playing_players:
        now_playing_players.add(user.id)
        if reaction.message.author.permissions_in(reaction.message.channel).manage_messages:
            await reaction.message.clear_reactions()
        await reaction.message.add_reaction('⬅️')
        await reaction.message.add_reaction('⬆️')
        await reaction.message.add_reaction('➡️')
        await reaction.message.add_reaction('⬇️')
        await reaction.message.add_reaction('↪️')
        await reaction.message.add_reaction('↩️')
        await reaction.message.add_reaction('🇸')
        await reaction.message.add_reaction('🗑️')
        print(now_playing_players)
        await TETRIS.GAME_START(reaction.message, user)
        now_playing_players.discard(user.id)
    elif reaction.message.author.id == 671605558666592259 and reaction.message.embeds and reaction.message.embeds[0].title == 'TESTGAME('+str(user.id)+')' and reaction.message.embeds[0].description == 'STAND BY' and user.id not in now_playing_players:
        now_playing_players.add(user.id)
        if reaction.message.author.permissions_in(reaction.message.channel).manage_messages:
            await reaction.message.clear_reactions()
        await reaction.message.add_reaction('⬅️')
        await reaction.message.add_reaction('⬆️')
        await reaction.message.add_reaction('➡️')
        await reaction.message.add_reaction('⬇️')
        await reaction.message.add_reaction('↪️')
        await reaction.message.add_reaction('↩️')
        await reaction.message.add_reaction('🇸')
        await reaction.message.add_reaction('🗑️')
        print(now_playing_players)
        await TESTGAME.GAME_START(reaction.message, user)
        now_playing_players.discard(user.id)