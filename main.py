from requests import get, post
import discord
from discord import Colour, Embed, File, Member, Reaction
from discord.ext import tasks, commands
from discord.ext.commands import Bot, Cog, Context, command
import time
from bs4 import BeautifulSoup
import random
userAgents = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"]


headers = {
    'User-Agent': f'{random.choice(userAgents)}'
}
token = "NzM1ODUxMjcwNTY0NDc5MDE5.XxmQ5g.ANrhIxErYM6HWqxaIjMMOZ8wPGE"

## Header information

client = commands.Bot(command_prefix='', case_insensitive=True)
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))

@client.command()
async def check(ctx, type):
    sending = await ctx.send(f"Sending price request to `https://www.binance.com/en/trade/{type}_BUSD?type=spot`<a:loading2:835515993236308018>")
    url = f'https://www.binance.com/en/trade/{type}_BUSD?type=spot'
    await ctx.trigger_typing()
    page = get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find('title').get_text()
    print(title)
    if title == "Binance":
        embed = discord.Embed(title=f"{type} $", description="This crypto currency doesnt exist!\nNice job being stupid")
        embed.set_thumbnail(url="https://consumer.healthday.com/media-library/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZSI6Imh0dHBzOi8vYXNzZXRzLnJibC5tcy8yMzYyNzAyMy9vcmlnaW4uanBnIiwiZXhwaXJlc19hdCI6MTY2ODY0NDM2N30.warFRW3WI9jLil0TTj26K_HQpsGexdlgkfR7TPENbos/image.jpg?width=1245&quality=85&coordinates=0%2C74%2C0%2C75&height=700")
        embed.set_footer(text="laugh at this user")
        await sending.edit(content="LOL LAUGH AT THIS USER <a:XD:857399549295329280>")
    else:
        embed = discord.Embed(title=f"{type} $", description="$"+title.split(" ")[0]+f" USD\n\nhttps://www.binance.com/en/trade/{type}_BUSD?type=spot", url=f"https://www.binance.com/en/trade/{type}_BUSD?type=spot")
        embed.set_thumbnail(url=f"https://crypto.com/price/coin-data/icon/{type.upper()}/color_icon.png")
        embed.set_footer(text="Made by leki#6796 using BeautifulSoup")
        await sending.edit(content="Done! <a:check:857397222274236426>")
    await ctx.send(embed=embed)
@client.command()
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2 - time_1) * 1000)
    await ctx.send(f"Pong! `{ping}ms`")
    print(f"Milisecond response time {ping}")

client.run(token)
