import requests
from pprint import pprint

def get_weather(api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': "Moscow",
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        res = requests.get(url, params=params, timeout=5)

        if res.status_code == 200:

            data = res.json()

            weather_info = {
                'город': data['name'],
                'температура': f"{data['main']['temp']}°C",
                'ощущается_как': f"{data['main']['feels_like']}°C",
                'описание_погоды': data['weather'][0]['description'],
                'влажность': f"{data['main']['humidity']}%",
                'ветер': f"{data['wind']['speed']} м/с"
            }

            return weather_info, data
        
        elif res.status_code == 401:
            print("Неверный ключ")
            return
        
        elif res.status_code == 404:
            print("Город не найден")
            return
        
    except requests.exceptions.Timeout:
        print("Время ответа вышло")
        return
    
def main():
    api = "16b9f6bd8aead0b8d4c103ba97f435de"

    while True:
        choice = input("0 - для выхода: ")

        weather, data = get_weather(api)

        if choice == "0":
            print("До свидания")
            return

        elif choice == "+":
            pprint(data)

        if weather:
            print("\n----------------------------------")
            print(f"Город: {weather['город']}")
            print(f"Температура: {weather['температура']} (ощущается как {weather['ощущается_как']})")
            print(f"Погода: {weather['описание_погоды']}")
            print(f"Влажность: {weather['влажность']}")
            print(f"Ветер: {weather['ветер']}")
        else:
            print("Не получилось получить данные")

if __name__ == "__main__":
    main()
