## Начало работы 
### Склонируйте репозиторий:
```sh
& git clone https://github.com/lineisover/library
```
### Преходим в папку проекта:
```sh
& cd library
```
### Установить виртуальное окружение:
```sh
& py -3.11 -m venv .venv
```
`-3.11` - версия python  
`.venv` - путь к виртуальному окружению  

### Активировать виртуальное окружение:  
- Для Windows
```sh
& .venv\Scripts\activate.ps1
```
- Для Linux и MacOS
```sh
& source venv/bin/activate
```
### Устанавливаем зависимости:
```sh
& pip install -r requirements.txt
```
### Запускаем проект:
```sh
& python library\manage.py runserver
```
Profit!!!  
По умолчанию сервер будет запущен по адресу [127.0.0.1:8000](http://127.0.0.1:8000)
