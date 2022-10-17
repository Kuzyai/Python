import requests
APPID = "067302bba9e49593f082b73d5d7d1f8e"
URL_BASE = "http://api.openweathermap.org/data/2.5/"


def current_weather(q: str = "Chicago", appid: str = APPID, units: str = 'metric', lang: str = 'ru') -> dict:
    return requests.get(URL_BASE + "weather", params=locals()).json()


if __name__ == "__main__":
    from pprint import pprint
    while True:
        location = input("Enter a location: ").strip()
        if location:
            pprint(current_weather(location))
        else:
            break
