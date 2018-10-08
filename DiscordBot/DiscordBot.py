
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
    # 「eggplant」で始まるか調べる
    if message.content.startswith("eggplant"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            # m = "おはようございます" + message.author.name + "さん！"
            m = ":eggplant:"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)

client.run("NDk4NzQzNDkxODYyNTkzNTQ2.DpyMUw.E_QptUvTp0bg7OFFxcykRT5gOtM")