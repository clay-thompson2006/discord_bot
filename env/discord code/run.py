import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.members = True # Enable member intents
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


#verification system

@bot.command()
async def start_verification(ctx):
    # Generate a random 6-digit code
    code = ''.join(random.choices('0123456789', k=6))
    # Send the verification message
    await ctx.send(f"Please choose the word 'correct' and enter the following code: {code}")
    # Store the code in the user's data
    ctx.author.data['verification_code'] = code

@bot.command()
async def verify(ctx, *, message):
    # Check if the user has a verification code stored
    if 'verification_code' in ctx.author.data:
        # Check if the message contains the word 'correct' and the correct code
        if 'correct' in message and ctx.author.data['verification_code'] in message:
            # Find the verified role
            verified_role = discord.utils.get(ctx.guild.roles, name="Verified")
            # Assign the verified role to the user
            await ctx.author.add_roles(verified_role)
            await ctx.send(f"{ctx.author.mention}, you have been verified!")
        else:
            await ctx.send("Incorrect code or message. Please try again.")
    else:
        await ctx.send("You have not started the verification process. Use !start_verification to begin.")


#welcome message

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='welcome')
    if channel is not None:
        embed = discord.Embed(title="Welcome!", description=f"Welcome {member.mention} to our server!", color=discord.Color.green())
        embed.set_footer(text="Welcome to our server!")
        await channel.send(embed=embed)

#embed message

class embedcreator(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    @commands.command(description="create a simple embed!") 
    async def embed(self, ctx):
        # Your embed creation logic here
        pass



class embedCreator(discord.ui.Modal):
    def __init__(self, *args, kwargs):
        super().init(
            discord.ui.InputText(
                label="embed title",
                placeholder="title"
            ),
            discord.ui.InputText(
                label="embed description",
                placeholder="description"
            ),
            discord.ui.InputText(
                label="image url",
                placeholder="URL",
                required=False
            ),
            *args,
            kwargs
        )
    async def callback(self, interaction: discord.Interaction):
        client=interaction.client
        guild=interaction.guild

        em = discord.Embed(
            title=self.children[0].value,
            description=self.children[1].value,
            color=discord.Color.blurple()

        )
        if self.children[2].value is not None:
            try:
                em.set_image(url=self.children[2].value)
            except:
                return
        else:
            return

        await interaction.channel.send(embed=em)
        await interaction.response.send_message("send the embed successfully", ephemeral=True)

bot.add_cog(embedcreator(bot))



bot.run('MTE5MTU3OTA2ODgxOTMxMjY0MA.GD2S9V.wi5hUOB4qbTRV8ghQ3BESnCnIzwG0ujFMnlH2w')