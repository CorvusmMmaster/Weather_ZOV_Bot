import  requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city,open_weather_token):


    code_smile = {
        "Clear": "Ясно \U0001F31E",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U0001F327",
        "Drizzle": "Дождь \U0001F327",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
    }


    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)
        city=data['name']
        cur_weather = data['main']['temp']
        weather_description = data["weather"][0]["main"]
        if weather_description in code_smile:
            wd=code_smile[weather_description]
        else:
            wd="Даже описывать не хочу"
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp=datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp=datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day=datetime.datetime.fromtimestamp(data['sys']['sunset'])-datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        print (f"Сегодня: {datetime.datetime.now().strftime('%Y-%m-%d; %H:%m')}\n"
            f"Погода в городе: {city}\n"
            f"Температура: {cur_weather}C°, {wd}\n"
            f"Влажность: {humidity}%\n"
            f"Ветер: {wind}м/с\n"
            f"Восход солнца: {sunrise_timestamp}\n"
            f"Закат солнца: {sunset_timestamp}\n"
            f"Продолжительность часового дня: {length_of_the_day}\n"
              )


    except Exception as ex:
        print("Перепроверьте название города")

def main():
    city=input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()