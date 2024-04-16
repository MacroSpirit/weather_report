import requests
import json
from data_analysis import weather_data_analysis
from database import Session, WeatherDataTable, create_table
from info import API_KEY, BULK_FILE_NAME
import time

#получение данных о погоде
def get_weather_data():
    url = f'https://bulk.openweathermap.org/snapshot/{BULK_FILE_NAME}?appid={API_KEY}'
    data = requests.get(url)
    return weather_data_analysis(data)


def add_data():
    session = Session()
    create_table()
    while True:
        weather_data = get_weather_data()
        if weather_data:
            new_record = WeatherDataTable(
                data=weather_data
            )
            session.add(new_record)
        session.commit()
        time.sleep(3600)


add_data()
