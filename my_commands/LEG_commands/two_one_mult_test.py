# two_one_exam
import discord
from typing import Dict, List, Optional
import random
import asyncio

channel_id: Optional[int] = None
score: Dict[discord.User, int] = {}
kaitous: Dict[discord.User, str] = {}


async def two_one_exam(m: List[str], message: discord.Message) -> None:
    n: int = 200
    if len(m) >= 3:
        if not m[2].isdigit():
            await message.reply("回数を正しく設定してください")
            return
        else:
            n = int(m[2])
            if n < 10 or n > 1000:
                await message.reply('nは10以上1000以下を設定してください')
                return
    global channel_id, score, kaitous
    print(f"??{channel_id}??")
    if channel_id is not None:
        await message.reply("今やってます")
    else:
        for i in range(1, n + 1):
            channel_id = message.channel.id
            a: int
            if i < n * 0.9:
                a = random.randrange(10, 100)
            else:
                a = random.randrange(100, 1000)
            b: int = random.randrange(1, 10)
            temp: discord.Message = await message.channel.send(f"【{i}問目】{a}×{b}=?")
            ans: str = f"{a * b}"
            flag: bool = False
            for j in range(3000):
                await asyncio.sleep(0.001)
                for kaitou_user in kaitous:
                    if kaitous[kaitou_user] == ans:
                        await temp.edit(f"【{i}問目】{a}×{b}={a * b}  正解: {kaitou_user.display_name}")
                        if kaitou_user not in score:
                            score[kaitou_user] = 1
                        else:
                            score[kaitou_user] += 1
                        kaitous = {}
                        flag = True
                        break
                if flag:
                    break
            if j == 2999:
                await temp.edit(f"【{i}問目】{a}×{b}={a * b}  時間切れ")
        seiseki: str = ""
        winner: Optional[discord.User] = None
        for kaitou_user in score:
            seiseki += f"{kaitou_user.display_name}: {score[kaitou_user]}\n"
            if winner is None or score[kaitou_user] > score[winner]:
                winner = kaitou_user
        if winner is None:
            seiseki += "winner is none"
        else:
            seiseki += f"winner: {winner.display_name}"
        await message.channel.send(seiseki)
        channel_id = None
        score = {}
