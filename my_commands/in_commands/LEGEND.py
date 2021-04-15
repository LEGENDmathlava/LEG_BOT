#LEGEND
#'LEGEND'

import discord
from typing import Union, Optional
async def LEGEND(message:discord.Message)->None:
    from legbot_unchi import client
    channel:Optional[Union[discord.abc.GuildChannel, discord.abc.PrivateChannel]] = client.get_channel(378912400113664002)
    if message.channel != channel:
        if channel is not None:
            await channel.send('<@!344849211910651905>')
            await channel.send(message.content)