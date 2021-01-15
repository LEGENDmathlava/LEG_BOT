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
    try:
        await my_command(message)
    except IndexError:
        print("=============IndexError=============")
        print(message.content)
        print("====================================")
    if 'ECHO_FLOWER' not in message.content:
        f = open('ECHO_FLOWER', mode='w')
        f.write(message.content)
        f.close()
    

@client.event
async def on_reaction_add(reaction, user):
    print('test2')

@client.event
async def on_ready():
    print('on_ready')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)