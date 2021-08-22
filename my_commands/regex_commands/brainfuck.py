# brainfuck
# r'^[><+-.,[\]]+(\n# INPUT\n[\s\S]*)?$'

import discord
import time
from typing import Dict


async def brainfuck(message: discord.Message) -> None:
    print('========brain f*ck========')
    temp = message.content.split('\n# INPUT\n')
    source = temp[0]
    input_string = '\n# INPUT\n'.join(temp[1:])
    brancket_depth = 0
    for ch in source:
        if ch == '[':
            brancket_depth += 1
        if ch == ']':
            brancket_depth -= 1
        if brancket_depth < 0:
            return
    if brancket_depth != 0:
        return
    await message.reply('brainf*ckを検出しました')
    if not input_string.isascii():
        await message.channel.send('現在非ASCII文字には対応していません')
        return
    source_ptr = 0
    mem: Dict[int, int] = {}
    mem_ptr = 0
    step = 0
    output_string = ''
    embed = discord.Embed(title='brainf*ck', description='START')
    embed.add_field(name='source_ptr', value=source_ptr)
    embed.add_field(name='mem_ptr', value=mem_ptr)
    embed.add_field(name='step', value=step)
    embed.add_field(name='source', value='```\n' + source_extract(source, source_ptr) + '\n' + ' ' * 13 + '^' + ' ' * 13 + '\n```', inline=False)
    embed.add_field(name='mem', value='```\n' + mem_extract(mem, mem_ptr) + '\n' + ' ' * 13 + '^' + ' ' * 13 + '\n```', inline=False)
    embed.add_field(name='input_buffer', value='```\n' + input_string[:1016] + '\n```', inline=False)
    embed.add_field(name='output_buffer', value='```\n' + output_string[-1016:] + '\n```', inline=False)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed_message = await message.channel.send(embed=embed)
    brancket_taiou = {}
    brancket_stack = []
    for i in range(len(source)):
        ch = source[i]
        if ch == '[':
            brancket_stack.append(i)
        if ch == ']':
            left = brancket_stack.pop(len(brancket_stack) - 1)
            right = i
            brancket_taiou[left] = right
            brancket_taiou[right] = left
    print(brancket_taiou)
    for i in range(500):
    # while True:
        ch = source[source_ptr]
        if ch == '+':
            if mem_ptr not in mem:
                mem[mem_ptr] = 1
            else:
                mem[mem_ptr] = (mem[mem_ptr] + 1) % 0x100
        elif ch == '-':
            if mem_ptr not in mem:
                mem[mem_ptr] = 0xff
            else:
                mem[mem_ptr] = (mem[mem_ptr] - 1) % 0x100
        elif ch == '>':
            mem_ptr += 1
        elif ch == '<':
            mem_ptr -= 1
        elif ch == '.':
            if mem_ptr not in mem:
                output_string += chr(0)
            else:
                output_string += chr(mem[mem_ptr])
        elif ch == ',':
            if not bool(input_string):
                break
            else:
                mem[mem_ptr] = ord(input_string[0])
                input_string = input_string[1:]
        elif ch == '[':
            if mem_ptr not in mem or mem[mem_ptr] == 0:
                source_ptr = brancket_taiou[source_ptr]
        elif ch == ']':
            if mem_ptr in mem and mem[mem_ptr] != 0:
                source_ptr = brancket_taiou[source_ptr]
        step += 1
        source_ptr += 1
        if source_ptr >= len(source):
            break
        await paint(message, embed_message, source, source_ptr, mem, mem_ptr, step, input_string, output_string, True)
    await paint(message, embed_message, source, source_ptr, mem, mem_ptr, step, input_string, output_string, False)
    if bool(output_string):
        await message.channel.send(output_string)
    print('========----------========')


async def paint(message: discord.Message, embed_message: discord.Message, source: str, source_ptr: int, mem: Dict[int, int], mem_ptr: int, step: int, input_string: str, output_string: str, flag: bool) -> None:
    description = 'running' if flag else 'end'
    for _ in range(100):
        time.sleep(0.01)
    embed = discord.Embed(title='brainf*ck(500まで)', description=description)
    embed.add_field(name='source_ptr', value=source_ptr)
    embed.add_field(name='mem_ptr', value=mem_ptr)
    embed.add_field(name='step', value=step)
    embed.add_field(name='source', value='```\n' + source_extract(source, source_ptr) + '\n' + ' ' * 13 + '^' + ' ' * 13 + '\n```', inline=False)
    embed.add_field(name='mem', value='```\n' + mem_extract(mem, mem_ptr) + '\n' + ' ' * 13 + '^' + ' ' * 13 + '\n```', inline=False)
    embed.add_field(name='input_buffer', value='```\n' + input_string[:1016] + '\n```', inline=False)
    embed.add_field(name='output_buffer', value='```\n' + output_string[-1016:] + '\n```', inline=False)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await embed_message.edit(embed=embed)


def source_extract(source: str, source_ptr: int) -> str:
    return (' ' * 13 + source + ' ' * 14)[source_ptr: 27 + source_ptr]


def mem_extract(mem: Dict[int, int], mem_ptr: int) -> str:
    s = ''
    for i in range(mem_ptr - 4, mem_ptr + 5):
        if i not in mem:
            s += '00 '
        else:
            s += f'{mem[i]:02x} '
    return s
