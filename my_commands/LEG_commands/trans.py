#trans
async def trans(m, message):
    if message.reference:
        message2 = await message.channel.fetch_message(message.reference.message_id)
        if message2.content == '':
            await message.channel.send('文字を一つ以上必要です')
            return
        my_str = message2.content
    else:
        if len(m) < 3:
            await message.channel.send('文字を一つ以上必要です')
            return
        my_str = message.content[message.content.find(m[2], message.content.find(m[1])+5):]
    s = ''
    my_str = my_str.encode('utf-8')
    if len(my_str) >= 644:
        await message.channel.send('長すぎです')
        return
    for chnum in my_str:
        s += '%' + f'{chnum:02x}'.upper()
    await message.channel.send(f'https://translate.google.co.jp/?hl=ja&sl=auto&tl=ja&text={s}&op=translate')
