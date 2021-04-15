#paiza_cpp
#'<iostream>'
import discord
import time
import requests

async def paiza_cpp(message:discord.Message)->None:
    print(message.content)
    if not message.content.startswith('#include<iostream>') and not message.content.startswith('#include <iostream>') or message.author.bot:
        return
    temp:list[str] = message.content.split('\n# INPUT\n')
    source = temp[0]
    input_string = '\n# INPUT\n'.join(temp[1:])
    url = 'http://api.paiza.io'
    params = {
        'source_code': source,
        'language': 'cpp',
        'input': input_string,
        'api_key': 'guest',
    }
    response = requests.post(
        url + '/runners/create',
        json=params
    )
    print(response)
    id = response.json()['id']
    time.sleep(2.0)
    params = {
        'id': id,
        'api_key': 'guest',
    }
    response = requests.get(
        url + '/runners/get_details',
        json=params
    )
    print(response)
    result = response.json()
    print(result)
    if bool(result['stdout']):
        await message.reply(result['stdout'])
