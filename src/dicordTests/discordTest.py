# Work with Python 3.6
import discord

TOKEN = 'NzM3OTM2OTc4NzM3MzY1MDYz.XyEnXQ.4eTnxdrJ3KkNk-IpeQ8Bt2xv4gM'
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Bonjour a toi aussi mon cher {0.name}!'.format(message.author)
        await message.channel.send(msg)
        # await client.send_message(message.channel, msg)

    # une autre commande : jeu du pendu
    elif message.content.startswith('!pendu'):
        msg = 'Tu veux jouer au pendu , mon cher {0.name} ? OK!'.format(message.author)
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as :')
    print('client.user.name [', client.user.name, ']')
    print('client.user.id [', client.user.id, ']')
    print('------')


client.run(TOKEN)




