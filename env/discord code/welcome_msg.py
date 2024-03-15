import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

class Welcome(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
      # replace CHANNEL_ID with the id of the channel where you want to send the welcome message
      channel = bot.get_channel(1191585965043617815)
      if channel is not None:
          await channel.send(f'Welcome {member.mention}.')

bot.add_cog(Welcome(bot))
bot.run('MTE5MTU3OTA2ODgxOTMxMjY0MA.GD2S9V.wi5hUOB4qbTRV8ghQ3BESnCnIzwG0ujFMnlH2w')