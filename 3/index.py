import discord
token = "토큰"
client = discord.Client()

@client.event
async def on_ready():
    print("도배시작")
    print(client.user)
    print("레츠 고도리")

@client.event
async def on_message(message):

    number = 10
    while number > 0:
        if message.content == "!도배":
            await message.channel.send("도배" * 1000)
        if message.content == "!도배":
            await message.channel.send("도배" * 1000)
        if message.content == "!도배":
            await message.channel.send("도배" * 1000)

client.run(token)
