#naam = "henk"
#anderenaam = ""

#def Calculaties(naam):
    #z = x * y
 #   naam = naam
  #  anderenaam = "Jan"
  #  anderenaam = anderenaam

  #  return anderenaam

#Calculaties(naam)
#uitkomst = Calculaties(anderenaam)
#print(uitkomst)

from buienradar.buienradar import (get_data, parse_data)
from buienradar.constants import (CONTENT, RAINCONTENT, SUCCESS)
import discord
import os
client = discord.Client()


inputlat = "leeg"
inputlong = "leeg"
inputlocatie = "leeg"


def test(inputlocatie):

    inputlocatie = inputlocatie
    anderlocatie = "Heide"
    anderlocatie = anderlocatie

    return anderlocatie
    
anderelocatie = ""
anderelocatie = test(anderelocatie)

@client.event
async def on_ready():
    print('Bot online')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.content.startswith('weer venray'):
        inputlat = float(51.525287)
        inputlong = float(5.973349)
        inputlocatie = "Venray"

        test (inputlocatie)

        print(anderelocatie)

client.run("ODIwNjAyMzY4OTU3NDgwOTYx.YE3jgg.4kM_EeRJU3ZsdUHQ7EfpuegOmo4")