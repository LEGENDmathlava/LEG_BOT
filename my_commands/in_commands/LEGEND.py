#LEGEND
#'LEGEND'

import discord
async def LEGEND(message:discord.Message):
    from legbot_unchi import client
    channel:Optional[Union[discord.abc.GuildChannel, discord.abc.PrivateChannel]] = client.get_channel(378912400113664002)
    if message.channel != channel:
        await channel.send('<@!344849211910651905>')
        await channel.send(message.content)