# escape
import discord
from typing import List


async def escape(m: List[str], message: discord.Message) -> None:
    if message.author.bot:
        return
    if message.reference:
        message2 = await message.channel.fetch_message(message.reference.message_id)
        s = message2.content
        escape_string = ''
        for ch in s:
            if ch.isascii() and not ch.isalnum() and ch != ' ' and ch != '\n':
                escape_string += '\\'
            escape_string += ch
        if escape_string != '':
            await message.channel.send(escape_string[:2000])
            s = m[0]
