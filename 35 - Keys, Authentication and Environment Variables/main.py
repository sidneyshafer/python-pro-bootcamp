import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "77839165a69dfeed9049425c67f298db"
account_sid = 'AC0d9bf240e173661c3e563ef2a9bd2fe6'
auth_token = '497614f508acf2ff3e479c0a30b85e13'

weather_params = {
    "q": "Chaska",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["weather"][0]["id"]
weather_main = weather_data["weather"][0]["main"].lower()

client = Client(account_sid, auth_token)

if weather_id < 700:
    message = client.messages.create(
        body=f"Bring an umbrella. There is {weather_main} outside today :( .",
        from_='+18556476354',
        to='+19525670362'
    )
else:
    message = client.messages.create(
        body=f"No umbrella needed today! The weather is {weather_main} outside today :) .",
        from_='+18556476354',
        to='+19525670362'
    )

print(message.status)

