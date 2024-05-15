import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def naber(ctx):
    await ctx.send('iyiyim sen nasılsın?')


@bot.command()
async def toplama(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(f'sonuç={left + right}')

@bot.command()
async def çıkarma(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(f'sonuç={left - right}')

@bot.command()
async def çarpma(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(f'sonuç={left * right}')

@bot.command()
async def bölme(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(f'sonuç={left / right}')

@bot.command()
async def üst(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(f'sonuç=  {left ** right}')

bot.run("YOUR DISCORD TOKEN")
    
    
