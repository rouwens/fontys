from buienradar.buienradar import (get_data, parse_data)
from buienradar.constants import (CONTENT, RAINCONTENT, SUCCESS)

# minutes to look ahead for precipitation forecast
# (5..120)
timeframe = 45

# gps-coordinates for the weather data
latitude = 52.1
longitude = 5.10

result = get_data(latitude=latitude,
                  longitude=longitude,
                  )

if result.get(SUCCESS):
    data = result[CONTENT]
    raindata = result[RAINCONTENT]

    result = parse_data(data, raindata, latitude, longitude, timeframe)

print(result)