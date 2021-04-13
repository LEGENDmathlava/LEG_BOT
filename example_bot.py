print(chr(7))
print(chr(7))
print(chr(7))
print(chr(7))
# インストールした discord.py を読み込む
import discord
import random
import sys
import datetime
from typing import Union

print(chr(7))
print(chr(7))
print(chr(7))
print(chr(7))

from legbot_unchi import *
from my_command import my_command
from reaction_command import reaction_command

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
b = False

# メッセージ受信時に動作する処理
num=random.randrange(100)+1000
@client.event
async def on_message(message:discord.Message):
    if message.author.id == 739586615487496274:
        return
    if message.channel.id == 534027499252744202:
        print(str(message.content) + '\n\n')
        if message.content[:3] == '.OX':
            print(chr(7))
            print(chr(7))
            print(chr(7))
            r = random.randrange(2)
            print(chr(7))
            print(chr(7))
            print(chr(7))
            await message.add_reaction(chr(11093 if r else 10060))
        elif message.content[:3] == '10分':
            print(chr(7))
            print(chr(7))
            print(chr(7))
            r = random.randrange(2)
            print(chr(7))
            print(chr(7))
            print(chr(7))
            if message.author.id==552020060449931284:
                await message.channel.send('10分ですね')

    await my_command(message)
    if 'ECHO_FLOWER' not in message.content:
        f = open('ECHO_FLOWER', mode='w')
        f.write(message.content)
        f.close()
    

@client.event
async def on_raw_reaction_add(payload:discord.RawMessageDeleteEvent):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    emoji = payload.emoji
    reactions = message.reactions
    for r in reactions:
        if r.emoji == emoji.name:
            reaction = r
            break
    user = client.get_user(payload.user_id)
    await reaction_command(reaction, user)

@client.event
async def on_ready():
    print('on_ready')

@client.event
async def on_typing(channel:discord.abc.Messageable, user:Union[discord.User, discord.Member], when:datetime.datetime):
    if channel.id == 740114205444931594:
        await channel.send(user.mention+'\nこんにちわ！！！！！')
        print(channel.guild)
    if channel.id == 804573278937153596 and not user.bot:
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')


@client.event
async def on_guild_channel_create(channel:discord.abc.GuildChannel):
    print('test34')
    if channel.guild.id == 739882359649992714 or channel.guild.id == 378912400113664000:
        await channel.send(channel.mention+'に一番乗り！！')

@client.event
async def on_guild_channel_update(before:discord.abc.GuildChannel, after:discord.abc.GuildChannel):
    print('test43')

@client.event
async def on_guild_channel_delete(channel:discord.abc.GuildChannel):
    if channel.guild.id == 739882359649992714:
        channel2 = client.get_channel(804573278937153596)
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')
        await channel2.send(channel.name+'を返せ！！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

#804573278937153596 荒らし
#740198572435308635 旧荒らし