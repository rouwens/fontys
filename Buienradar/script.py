from buienradar.buienradar import (get_data, parse_data)
from buienradar.constants import (CONTENT, RAINCONTENT, SUCCESS)
import configparser

config = configparser.ConfigParser()
config.read('/home/daan/Bureaublad/School/Github/fontys/Buienradar/config.ini')

tijd = config['settings']['tijd']
locatie = config['settings']['locatie']

def start(lati, longi, tijd):

                timeframe = int(tijd)

                latitude = float(lati)
                longitude = float(longi) 

                result = get_data(latitude=latitude,
                                longitude=longitude,
                                )

                if result.get(SUCCESS):
                    data = result[CONTENT]
                    raindata = result[RAINCONTENT]

                    result = parse_data(data, raindata, latitude, longitude, timeframe)

                print(result)

if locatie == "venray":
    start(lati = "51.525287", longi = "5.973349", tijd = tijd)

elif locatie == "eindhoven":
    start(lati = "51.450967", longi = "5.479683", tijd = tijd)

elif locatie == "hunsel":
    start(lati = "51.188768", longi = "5.813526", tijd = tijd)

else: 
    print ("Locatie niet herkend/ondersteund")

    