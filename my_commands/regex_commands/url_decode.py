# url_decode
# r'https?\S+\.\S'

import discord
import subprocess


async def url_decode(message: discord.Message) -> None:
    if message.author.id == 822513071062253598:
        decode_url = ''
        p = subprocess.Popen(['./perl-lib/url/decode.pl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, error = p.communicate(input=message.content.encode('utf-8'))
        decode_url += out.decode('utf-8')
        await message.reply(decode_url[:2000])
