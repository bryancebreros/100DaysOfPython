import os
import requests
from twilio.rest import Client

api_key = "0a417ad5a8f4b9d87c72193513ae9223"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
LAT = "19.432608" #CULIACAN -> "24.807390"
LON = "-99.133209" #culiacan ->-107.394440"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(ENDPOINT, params=weather_params)
data = response.json()["hourly"]
weather_data = data[:12]
weather_list = []
will_rain = False
for i in range(len(weather_data)):
    condition = weather_data[i]['weather'][0]['id']
    if condition < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Se aproximan lluvias.Recuerda salir con sombrilla 🌧☔',
        from_='+17622164918',
        to='+526673515718'
    )


print(message.status)

# if data["id"] < 700:
#     print("Llevar sombrilla!")