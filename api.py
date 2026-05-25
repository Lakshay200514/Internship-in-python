import requests

def weather_data(city):
    api_key = "ac97da7ae4f2875c3b14fdaf4cd084f5"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        print(data['main']['temp'])
    except requests.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
    return None

city = input("Enter a city name: ")
weather_data(city)