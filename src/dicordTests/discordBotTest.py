# Work with Python 3.6
import discord

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from src.dicordTests.DiscordBotCmd import DiscordBotCmd

TOKEN = 'NzM3OTM2OTc4NzM3MzY1MDYz.XyEnXQ.4eTnxdrJ3KkNk-IpeQ8Bt2xv4gM'
client = discord.Client()
bot = commands.Bot(command_prefix='!')  # define command decorator

botCmd = DiscordBotCmd()


@bot.command(pass_context=True)  # define the first command and set prefix to '!'
async def hi(ctx):
    msg = 'Bonjour a toi aussi mon cher {0.name}!'.format(ctx.author)
    await ctx.send(msg)


@bot.command(pass_context=True)
async def cmdlist(ctx):
    str1 = 'Cher {0.name}, voici les commandes :'.format(ctx.author)
    str2 = botCmd.list()
    resp = " ".join((str1, str2))
    await ctx.send(resp)


@bot.command(pass_context=True)
async def hangman(ctx):
    msg = 'Tu veux jouer au pendu , mon cher {0.name} ? OK!\n'.format(ctx.author)
    await ctx.send(msg)


@bot.command(pass_context=True)
async def time(ctx):
    msg = 'Tu veux la date et l heure mon ami {0.name} ? OK, la voici :\n'.format(ctx.author)
    resp = " ".join((msg, botCmd.time()))
    await ctx.send(resp)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        print('error:', error)
        return
    raise error


@bot.event  # print that the bot is ready to make sure that it actually logged on
async def on_ready():
    print('Logged in as:')
    print('bot.user.name [', bot.user.name, ']')
    print('bot.user.id [', bot.user.id, ']')
    print('------')


bot.run(TOKEN)  # run the client using using my bot's token
