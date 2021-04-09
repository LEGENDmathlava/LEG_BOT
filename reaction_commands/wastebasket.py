#wastebasket
#'🗑️'
import my_commands.LEG_commands.TETRIS_GAME.TETRIS_control as TETRIS
import my_commands.LEG_commands.TEST_GAME.TESTGAME_control as TESTGAME
async def wastebasket(reaction, user):
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')':
        await TETRIS.exit_game(reaction.message, user)
    elif reaction.message.embeds and reaction.message.embeds[0].title == 'TESTGAME('+str(user.id)+')':
        await TESTGAME.exit_game(reaction.message, user)
    elif reaction.message.author.id == 671605558666592259 and user.id != 671605558666592259:
        await reaction.message.delete()
