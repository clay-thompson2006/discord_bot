import discord
from discord.ext import commands

class EmbedCommands(commands.Cog):
 def __init__(self, bot):
    self.bot = bot

 @commands.command()
 async def embed(self, ctx, title, description):
    embed = discord.Embed(title=title, description=description, color=0x00ff00)
    embed.add_field(name="Field Name", value="Field Value", inline=False)
    await ctx.send(embed=embed)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
bot.add_cog(EmbedCommands(bot))
bot.run("MTE5MTU3OTA2ODgxOTMxMjY0MA.GD2S9V.wi5hUOB4qbTRV8ghQ3BESnCnIzwG0ujFMnlH2w")
