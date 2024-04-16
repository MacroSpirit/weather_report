import json
from top50_cities import get_top50_cities

#проверка городов по координатам
def verify_city(city):
    for c in top50_cities:
        if city['city']['coord']['lon'] == c['lon'] and city['city']['coord']['lat'] == c['lat']:
            return True
    return False

top50_cities = []

#группировка данных о городах
def weather_data_analysis(cities):
    weather_report = {}
    if not top50_cities:
        top50_cities = get_top50_cities()
    if weather_report:
        weather_report.clear()
    cities = [eval(line.strip('\n')) for line in file.readlines()]
    for city in cities:
        if city['city']['name'] in [city['name'] for city in top50_cities]:
            if verify_city(city):
                weather_report[city['city']['name']] = {'temp': city['main']['temp'],
                                                        'pressure': city['main']['pressure'],
                                                        'humidity': city['main']['humidity'],
                                                        'weather': city['weather']['main']}
    return weather_report


