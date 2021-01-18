#wastebasket
#'🗑️'
async def wastebasket(reaction, user):
    if reaction.message.author.id == 671605558666592259:
        await reaction.message.delete()
