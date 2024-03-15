import discord
from discord.ext import commands
from requests import get
import json

client = commands.Bot(command_prefix="!")

@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content)
    meme = discord.Embed(title=f"{data['title']}", color=discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)

client.run("MTE5MTU3OTA2ODgxOTMxMjY0MA.GD2S9V.wi5hUOB4qbTRV8ghQ3BESnCnIzwG0ujFMnlH2w")