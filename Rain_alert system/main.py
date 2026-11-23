import requests
import os

API_KEY =os.environ["API_KEY"]
LAT=6.619831
LON=3.322167

parameters = {
    "lat":LAT,
    "lon":LON,
    "cnt":4,
    "appid":API_KEY
}

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    notification = requests.post(url, data=payload)
    return notification.json()

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

will_rain = False


for info in weather_data:
    if info["weather"][0]["id"] < 531:
        will_rain=True


if will_rain:
    send_telegram("It's going to rain\nYou should bring an umbrella")
else:

    send_telegram("It's not going to rain")
