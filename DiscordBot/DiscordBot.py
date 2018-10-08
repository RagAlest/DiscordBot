
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # if the message starts from "eggplant"
    if message.content.startswith("eggplant"):
        # if the message send from bot, ignore it
        if client.user != message.author:
            # write a message
            m = ":eggplant:"
            # send the message to channel
            await client.send_message(message.channel, m)

client.run("NDk4NzQzNDkxODYyNTkzNTQ2.DpyMUw.E_QptUvTp0bg7OFFxcykRT5gOtM")