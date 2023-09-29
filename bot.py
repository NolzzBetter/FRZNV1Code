import discord
from discord.ext import commands
import random

allowed_users = [1, 2, 3]


valid_codes = set()

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def generate(ctx, amount: int):
    if ctx.author.id not in allowed_users:
        await ctx.send("You are not authorized to use this command.")
        return
    if amount <= 0:
        await ctx.send("Please specify a positive number of codes to generate.")
        return
    if amount >= 101:
        await ctx.send("A max of 100 codes can be generated at once.")
        return
    codes = []
    for i in range(amount):
        code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
        codes.append(f"`{code}`")
        valid_codes.add(code)
    embed = discord.Embed(title=f"{amount} Codes Generated", color=0x0000FF)
    embed.add_field(name="Codes:", value='\n'.join(codes), inline=False)
    await ctx.send(embed=embed)

@client.command()
async def redeem(ctx, code: str):
    if code in valid_codes:
        valid_codes.remove(code)
        await ctx.send(f"Code Redeemed!")
    else:
        await ctx.send(f"code invalid.")

client.run('bot_token')
