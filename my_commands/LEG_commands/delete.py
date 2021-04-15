#delete
import discord
from typing import List
a = b = False
async def delete(m:List[str], message:discord.Message)->None:
    global a
    global b
    if not a:
        if message.channel.id == 740198572435308635:
            a = True
            await message.channel.send('削除開始')
            while True:
                print('準備中')
                messages = await message.channel.history(limit=3000, oldest_first=True).flatten()
                print('逆順中')
                messages.reverse()
                i=0
                for message in messages:
                    try:
                        await message.delete()
                    except:
                        print('error')
                        pass
                    print(i, 'test', message.content)
                    i += 1
    elif not b:
        if message.channel.id == 740198572435308635:
            b = True
            await message.channel.send('削除開始')
            while True:
                print('準備中')
                messages = await message.channel.history(limit=10000, oldest_first=False).flatten()
                print('逆順中')
                messages.reverse()
                for message in messages:
                    await message.delete()
                    print('test', message.content)
    else:
        await message.channel.send('削除開始できませんでした')