import json


#поиск крупнейших городов из файла
def get_cities():
    top_cities = []
    with open('current.city.list.json', 'r', encoding='utf-8') as file:
        cities = json.load(file)
        ordered_cities = sorted(
            cities,
            key=lambda x: x['stat']['population'],
            reverse=True
        )
        counter = 0
        for city in ordered_cities:
            if counter < 50:
                top_cities.append(
                    {'name': city['name'],
                    'population': city['stat']['population'],
                    'lon': city['coord']['lon'],
                    'lat': city['coord']['lat']}
                )
                counter += 1
    return top_cities
