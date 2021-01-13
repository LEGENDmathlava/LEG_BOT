#in_command
from my_commands.in_commands.aaaaa import aaaaa 
from my_commands.in_commands.good_night import good_night 
from my_commands.in_commands.heysiri import heysiri 
from my_commands.in_commands.LEGEND import LEGEND 
from my_commands.in_commands.mohumohu import mohumohu 
from my_commands.in_commands.poponta import poponta 
async def in_command(message):
    if 'ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁﾁﾁﾌﾞﾘﾘｲﾘﾌﾞﾌﾞﾌﾞﾌﾞｩｩｩｩｯｯｯ' in message.content:
        await aaaaa(message)
    if 'おやすみ' in message.content:
        await good_night(message)
    if 'Hey Siri' in message.content:
        await heysiri(message)
    if 'LEGEND' in message.content:
        await LEGEND(message)
    if 'もふもふ' in message.content:
        await mohumohu(message)
    if chr(129300) in message.content:
        await poponta(message)
