#good_night
#'おやすみ'
import sys
async def good_night(message):
    await message.add_reaction(chr(0x1F1F4))
    await message.add_reaction(chr(0x1F1FE))
    await message.add_reaction(chr(0x1F1E6))
    await message.add_reaction(chr(0x1F1F8))
    await message.add_reaction(chr(0x1F1FA))
    await message.add_reaction(chr(0x1F1F2))
    await message.add_reaction(chr(0x1F1EE))
    sys.exit()