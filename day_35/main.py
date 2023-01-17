import requests
from twilio.rest import Client

QWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "f03f939d9ac5a94863025e928b0e784e"
account_sid = "AC18d6076e99cda0a2fb1bf0c75a8604d6"
auth_token = "b7b95484981824da194ffc08b9cf6dd6"

weather_params = {
    "lat": 51.9457,
    "lon": 33.9348,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(QWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["hourly"][0:12]

for index in range(12):
    weather_id = weather_data[index]["weather"][0]["id"]
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                body="It's going to rain today. Remember to bring an unmbrella.",
                from_="+17622426721",
                to="*************"
            )    
        print(message.status)