Эта программа предназначена для получения данных о погоде в 50 крупнейших городах мира.
Данные забираются каждый час и сохраняются в базу данных.
Для успешной работы приложения необходима плантная версия на сайте https://openweathermap.org/ ,
так как программа забирает данные о погоде сразу в одном файле, а не по отдельности.
Требуется заменить переменную API_KEY в файле info.py на уникальный ключ из профиля с сайта.
Для запуска приложения необходимо установить виртуальное окружение, а затем его активировать:
python -m venv venv
.\venv\Scripts\activate
потом установить зависимости по команде :
pip install -r .\requirements.txt , 
а затем запустить файл main.py
