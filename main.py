import re

import discord
import random

import talk

TOKEN2 = ''

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bejelentkezve mint {0.user}'.format(client))
    talk.openfile()
    print("opened")


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if user_message.lower() == '!r':
        talk.openfile()
        print("opened")
        await message.channel.send('opened')
        return
    if user_message.lower().startswith('add!'):
        user_message = re.split(r'!',user_message)[1]
        talk.additem(user_message)
        print(user_message)
        await message.channel.send('added')
        return
    if user_message.lower() == '!binary':
        rand = random.random()
        await message.channel.send(round(rand))
        return
    if message.channel.name == 'bot':
        await message.channel.send(talk.get_response(user_message))
        return



    # commmands ----------
    if user_message.lower() == '!global':
        await message.channel.send('Mukodik')
        return



client.run(TOKEN2)