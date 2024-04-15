import json


#поиск крупнейших городов из файла
def get_top50_cities():
    top50_cities = []
    with open('current.city.list.json', 'r', encoding='utf-8') as file:
        cities = json.load(file)
        counter = 0
        for city in sorted(cities, key=lambda x: x['stat']['population'], reverse=True):
            if counter < 50:
                top50_cities.append({'name': city['name'],
                                    'population': city['stat']['population'],
                                     'lon': city['coord']['lon'],
                                     'lat': city['coord']['lat']})
                counter += 1
    return top50_cities
