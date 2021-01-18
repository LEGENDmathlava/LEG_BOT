print(chr(7))
print(chr(7))
print(chr(7))
print(chr(7))
# インストールした discord.py を読み込む
import discord
import random
import sys

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
async def on_message(message):
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
async def on_reaction_add(reaction, user):
    await reaction_command(reaction, user)

@client.event
async def on_ready():
    print('on_ready')

@client.event
async def on_typing(channel, user, when):
    if channel.id == 740114205444931594:
        await channel.send(user.mention+'\nこんにちわ！！！！！')
        print(channel.guild)
    if channel.id == 740198572435308635:
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
        await channel.send(user.mention+'\n荒らすな')
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

@client.event
async def on_guild_channel_create(channel):
    if channel.guild.id == 739882359649992714:
        await channel.send(channel.mention+'に一番乗り！！')

@client.event
async def on_guild_channel_delete(channel):
    if channel.guild.id == 739882359649992714:
        channel = client.get_channel(740198572435308635)
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')
        await channel.send(user.name+'を返せ！！')