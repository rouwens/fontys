import discord

client = discord.Client()

temp = "1000 °C"
windkracht = "23"

discord_temp = "Tempratuur: " + temp
discord_wind = "Windkracht: " + windkracht

@client.event
async def on_ready():
    print('Bot online')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.content.startswith('test'):
        await message.channel.send(discord_temp)
        await message.channel.send("-------------")
        await message.channel.send(discord_wind)

client.run("ODIwNjAyMzY4OTU3NDgwOTYx.YE3jgg.iIfK6afAIJ0T6lRMS3jihRU2TWY")
