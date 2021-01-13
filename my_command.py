from my_commands.in_command import in_command
from my_commands.kusa import 草
from my_commands.LEG import LEG
async def my_command(message):
    m = message.content.split()
    if (m[0] in globals()) and (str(globals()[m[0]])[:9] == '<function'):
        await globals()[m[0]](m, message)
    await in_command(message)
    