from requests import get, post
import discord
from discord import Colour, Embed, File, Member, Reaction
from discord.ext import tasks, commands
from discord.ext.commands import Bot, Cog, Context, command
from bs4 import BeautifulSoup
import random
userAgents = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"]
url = 'https://www.binance.com/en/trade/BTC_BUSD?type=spot'

headers = {
    'User-Agent': f'{random.choice(userAgents)}'
}
token = "token"
page = get(url, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
## Header information
title = soup.find('title').get_text()
client = commands.Bot(command_prefix='$', case_insensitive=True)
@client.command()
async def bitcoin(ctx):
    embed = discord.Embed(title="Bitcoin $", description="${}".format(title))
print("$"+title.split(" ")[0])
client.run(token)
