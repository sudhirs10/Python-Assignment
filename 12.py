#1
import requests
response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
print(data["value"])
#2
import requests

def get_weather(location, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    weather_text = data["weather"][0]["description"]
    temp_celsius = data["main"]["temp"]
    return weather_text, temp_celsius
def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter a location (city name): ")
    try:
        weather, temp = get_weather(location, api_key)
        print(f"The weather in {location} is: {weather}")
        print(f"The temperature is: {temp:.1f} degC")
    except Exception as e:
        print("Sorry, something went wrong:", e)
if __name__ == "__main__":
    main()
