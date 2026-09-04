import discord
from discord.ext import commands
import os
import random

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 로그인 완료!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # "로아 병신"이라고 하면
    if message.content == "로아 병신":
        responses = [
            "정답이다 연금술사!!",
            "아주 정확해",
            "당연한 것을"
        ]
        await message.channel.send(random.choice(responses))

    # "로아 시발새끼"라고 하면
    elif message.content == "로아 시발새끼":
        responses = [
            "쫌 많이 안타깝긴해",
            "레전드 로리충 병신 장애이긴해",
            "로아유충 삭제좀"
        ]
        await message.channel.send(random.choice(responses))

    await bot.process_commands(message)

bot.run(TOKEN)
