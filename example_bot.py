# インストールした discord.py を読み込む
import discord
import random
import datetime
from typing import Union
from legbot_unchi import client, TOKEN
from my_command import my_command
from reaction_command import reaction_command
import time

b = False

# メッセージ受信時に動作する処理
num = random.randrange(100) + 1000

@client.event
async def on_thread_join(thread: discord.Thread) -> None:
    await thread.join()
    if thread.guild.id == 739882359649992714:
        await thread.send(thread.mention + "Hello!!")

@client.event
async def on_message(message: discord.Message) -> None:
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
            if message.author.id == 552020060449931284:
                await message.channel.send('10分ですね')

    await my_command(message)
    if 'ECHO_FLOWER' in message.content:
        time.sleep(1)
    with open('ECHO_FLOWER', mode='w') as f:
        f.write('on_message\n')
        f.write(message.guild.name + '\n' if message.guild is not None else '\n')
        f.write(message.channel.name + '\n' if type(message.channel) == discord.TextChannel or type(message.channel) == discord.GroupChannel else 'DMchannel\n')
        f.write(message.author.nick + str(message.author.id) + '\n' if type(message.author) == discord.Member and message.author.nick is not None else message.author.name + str(message.author.id) + '\n')
        f.write(message.created_at.strftime('%x %X') + '\n')
        f.write(f'message_id:{message.id}\n')
        f.write(message.content)
        if message.reference and message.reference.message_id:
            referenced_message = await message.channel.fetch_message(message.reference.message_id)
            f.write('\n---- reference ----\n')
            f.write(referenced_message.content + '\n')
            f.write('-------------------')
        if message.attachments:
            f.write('\n==== attachments ====\n')
            for attachment in message.attachments:
                f.write(attachment.url + '\n')
            f.write('=====================')
        f.close()

    from my_commands.LEG_commands.two_one_mult_test import channel_id, kaitous
    if channel_id == message.channel.id:
        kaitous[message.author] = message.content

@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent) -> None:
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
    with open('ECHO_FLOWER', mode='w') as f:
        f.write('on_raw_reaction_add\n')
        f.write(message.guild.name + '\n' if message.guild is not None else '\n')
        f.write(message.channel.name + '\n' if type(message.channel) == discord.TextChannel or type(message.channel) == discord.GroupChannel else 'DMchannel\n')
        f.write(user.nick + str(user.id) + '\n' if type(user) == discord.Member and user.nick is not None else user.name + str(user.id) + '\n')
        f.write(message.created_at.strftime('%x %X') + '\n')
        f.write(f'message_id:{payload.message_id}\n')
        f.write(emoji.name + '\n')
        f.write('---- content ----\n')
        f.write(message.content + '\n')
        f.write('-----------------')
        f.close()


@client.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent) -> None:
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    emoji = payload.emoji
    user = client.get_user(payload.user_id)
    with open('ECHO_FLOWER', mode='w') as f:
        f.write('on_raw_reaction_remove\n')
        f.write(message.guild.name + '\n' if message.guild is not None else '\n')
        f.write(message.channel.name + '\n' if type(message.channel) == discord.TextChannel or type(message.channel) == discord.GroupChannel else 'DMchannel\n')
        f.write(user.nick + str(user.id) + '\n' if type(user) == discord.Member and user.nick is not None else user.name + str(user.id) + '\n')
        f.write(message.created_at.strftime('%x %X') + '\n')
        f.write(f'message_id:{payload.message_id}\n')
        f.write(emoji.name + '\n')
        f.write('---- content ----\n')
        f.write(message.content + '\n')
        f.write('-----------------')
        f.close()


@client.event
async def on_raw_message_delete(payload: discord.RawMessageDeleteEvent) -> None:
    if payload.cached_message:
        deleted_message = payload.cached_message
        with open('ECHO_FLOWER', mode='w') as f:
            f.write('on_raw_message_delete\n')
            f.write(deleted_message.guild.name + '\n' if deleted_message.guild is not None else '\n')
            f.write(deleted_message.channel.name + '\n' if type(deleted_message.channel) == discord.TextChannel or type(deleted_message.channel) == discord.GroupChannel else 'DMchannel\n')
            f.write(deleted_message.author.nick + str(deleted_message.author.id) + '\n' if type(deleted_message.author) == discord.Member and deleted_message.author.nick is not None else deleted_message.author.name + str(deleted_message.author.id) + '\n')
            f.write('不明\n')
            f.write(f'message_id:{payload.message_id}\n')
            f.write('---- deleted ----\n')
            f.write(deleted_message.content + '\n')
            if deleted_message.attachments:
                f.write('\n==== attachments ====\n')
                for attachment in deleted_message.attachments:
                    f.write(attachment.url + '\n')
                f.write('=====================\n')
            f.write('-----------------')
            f.close()
    else:
        guild = client.get_guild(payload.guild_id)
        channel = client.get_channel(payload.channel_id)
        with open('ECHO_FLOWER', mode='w') as f:
            f.write('on_raw_message_delete\n')
            f.write(guild.name + '\n' if guild is not None else '\n')
            f.write(channel.name + '\n' if type(channel) == discord.TextChannel or type(channel) == discord.GroupChannel else 'DMchannel\n')
            f.write('不明\n')
            f.write('不明\n')
            f.write(f'message_id:{payload.message_id}\n')
            f.write('---- deleted ----\n')
            f.write('-----------------')
            f.close()


@client.event
async def on_raw_message_edit(payload: discord.RawMessageUpdateEvent) -> None:
    if payload.cached_message:
        before_message = payload.cached_message
        message = await before_message.channel.fetch_message(payload.message_id)
    else:
        before_message = None
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
    await my_command(message)
    if 'ECHO_FLOWER' in message.content:
        time.sleep(1)
    with open('ECHO_FLOWER', mode='w') as f:
        f.write('on_raw_message_edit\n')
        f.write(message.guild.name + '\n' if message.guild is not None else '\n')
        f.write(message.channel.name + '\n' if type(message.channel) == discord.TextChannel or type(message.channel) == discord.GroupChannel else '\n')
        f.write(message.author.nick + str(message.author.id) + '\n' if type(message.author) == discord.Member and message.author.nick is not None else message.author.name + str(message.author.id) + '\n')
        f.write(message.created_at.strftime('%x %X') + '\n')
        f.write(f'message_id:{payload.message_id}\n')
        f.write('---- before ----\n')
        if before_message:
            f.write(before_message.content + '\n')
            if before_message.attachments:
                f.write('\n==== attachments ====\n')
                for attachment in before_message.attachments:
                    f.write(attachment.url + '\n')
                f.write('=====================\n')
        f.write('---- after  ----\n')
        f.write(message.content + '\n')
        if message.attachments:
            f.write('\n==== attachments ====\n')
            for attachment in message.attachments:
                f.write(attachment.url + '\n')
            f.write('=====================\n')
        f.write('----------------')
        f.close()


@client.event
async def on_ready() -> None:
    print('on_ready')


@client.event
async def on_typing(
        channel: discord.abc.Messageable,
        user: Union[discord.User, discord.Member],
        when: datetime.datetime) -> None:
    if channel.id == 740114205444931594:
        await channel.send(user.mention + '\nこんにちわ！！！！！')
        print(channel.guild)
    if channel.id == 804573278937153596 and not user.bot:
        await channel.send(user.mention + '\n荒らすな')
        await channel.send(user.mention + '\n荒らすな')
        await channel.send(user.mention + '\n荒らすな')


@client.event
async def on_guild_channel_create(channel: discord.abc.GuildChannel) -> None:
    print('test34')
    if channel.guild.id == 739882359649992714 \
            or channel.guild.id == 378912400113664000:
        await channel.send(channel.mention + 'に一番乗り！！')


@client.event
async def on_guild_channel_update(
        before: discord.abc.GuildChannel,
        after: discord.abc.GuildChannel) -> None:
    print('test43')


@client.event
async def on_guild_channel_delete(channel: discord.abc.GuildChannel) -> None:
    if channel.guild.id == 739882359649992714:
        channel2 = client.get_channel(804573278937153596)
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')
        await channel2.send(channel.name + 'を返せ！！')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

# 804573278937153596 荒らし
# 740198572435308635 旧荒らし
