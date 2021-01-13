#LEG
from my_commands.LEG_commands.DEBUG import DEBUG, MyNick
from my_commands.LEG_commands.DEUTSCH import DEUTSCH
from my_commands.LEG_commands.dict import char_NAME, RAND_CHAR, n_char_NAME
from my_commands.LEG_commands.ECHO import ECHO
from my_commands.LEG_commands.ECHO_FLOWER import ECHO_FLOWER
from my_commands.LEG_commands.HELP import HELP
from my_commands.LEG_commands.information import NAME, VERSION, ID, TOKEN
from my_commands.LEG_commands.SLEEP import SLEEP
from my_commands.LEG_commands.trans import trans

async def LEG(m, message):
    if (len(m) > 1) and (m[1] in globals()) and (str(globals()[m[1]])[:9] == '<function'):
        await globals()[m[1]](m, message)