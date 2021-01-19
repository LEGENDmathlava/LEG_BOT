#wastebasket
#'🗑️'
from my_commands.LEG_commands.TETRIS_GAME.TETRIS_control import exit_game
async def wastebasket(reaction, user):
    if reaction.message.embeds and reaction.message.embeds[0].title == 'TETRIS('+str(user.id)+')':
        await exit_game(reaction.message, user)
    elif reaction.message.author.id == 671605558666592259 and user.id != 671605558666592259:
        await reaction.message.delete()
