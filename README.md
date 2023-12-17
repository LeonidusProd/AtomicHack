## Начало работы 
### Склонируйте репозиторий:
```sh
& git clone https://github.com/LeonidusProd/AtomicHack.git
```
### Преходим в папку проекта:
```sh
& cd TextAnalytics
```
### Установить виртуальное окружение:
```sh
& py -3.12 -m venv .venv
```
`-3.11` - версия python  
`.venv` - путь к виртуальному окружению  

### Активировать виртуальное окружение:  
- Для Windows
```sh
& .venv\Scripts\activate.ps1
```
### Устанавливаем зависимости:
```sh
& pip install -r requirements.txt
```
### Запускаем проект:
```sh
& python manage.py runserver
```
Profit!!!  
По умолчанию сервер будет запущен по адресу http://127.0.0.1:8000
