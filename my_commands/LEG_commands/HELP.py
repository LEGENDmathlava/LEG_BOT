# HELP
import discord
from typing import List


async def HELP(m: List[str], message: discord.Message) -> None:
    await message.channel.send('What\'s the matter!! I help you!!')
