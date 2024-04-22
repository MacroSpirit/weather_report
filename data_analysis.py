import json
from info import top_cities

#проверка городов по координатам
def verify_city(city, top_cities):
    for c in top_cities:
        if (city['city']['coord']['lon'] == c['lon'] and
            city['city']['coord']['lat'] == c['lat']):
            return True
    return False


#группировка данных о городах
def weather_data_analysis(cities):
    weather_report = {}
    cities = [eval(line.strip('\n')) for line in file.readlines()]
    for city in cities:
        if city['city']['name'] in [city['name'] for city in top_cities]:
            if verify_city(city, top_cities):
                weather_report[city['city']['name']] = {
                    'temp': city['main']['temp'],
                    'pressure': city['main']['pressure'],
                    'humidity': city['main']['humidity'],
                    'weather': city['weather']['main']
                }
    return weather_report


