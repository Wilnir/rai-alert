import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a0ada5f7196a779abcbf65ec7b255181"

weather_params = {
        "lat": -23.112450,
        "lon": -47.216160,
        "appid": api_key,
        "exclude": "current,daily,minutely",
        }
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
        print("levar guarda-chuva")
else:
        print("dia de sol")

# response = requests.get(url="https://api.openweathermap.org"
#                         "/data/2.5/onecall?lat=-23.112450&lon=-47.216160&exclude={part}&appid=a0ada5f7196a779abcbf65ec7b255181")
