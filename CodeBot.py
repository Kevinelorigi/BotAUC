import discord
from discord.ext import commands
from urllib import parse, request
import re

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', description='A bot that does stuff.',intents=intents)


class MyClient(discord.Client):
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Doki El Favo"), status=discord.Status.online)
        print('Bot Listo.')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'Felipe':
        await message.channel.send('Comase de su mierda entonces y no invite a lol')

    if message.content.startswith('!'):
        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando no encontrado.')

@bot.command()
async def yt(ctx, *, search):
    results_base = "https://www.youtube.com/results?"
    q = parse.urlencode({"search_query": search})
    content = request.urlopen(results_base + q)

    results = re.findall('watch\?v=(.{11})', content.read().decode('utf-8'))
    result_URL = "https://www.youtube.com/watch?v=" + results[0]

    await ctx.send("Resultado de la búsqueda: " + result_URL)

bot.run('MTA0MzU1NDkxNjA3NTA0OTAyMA.G3fQBO.97oqYQqBMPxSjpMZ7oHaVCQXxjJpC-Z_Nq8seM')