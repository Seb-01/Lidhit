# Lidhit
Test task for Lidhit

## Инструкция по действиям для настройки и запуска приложения

### Шаг 1. Переходим (создаем) в директорию, куда хотим скачать проект.
### Шаг 2. Клонируем проект https://github.com/Seb-01/Lidhit, ветка master:

`yourPC:~$ git clone https://github.com/Seb-01/Lidhit -b master`

### Шаг 3. Создаем виртуальное окружение, чтобы изолироваться в проекте от других окружений. Название должно совпадать с названием проекта в GitHub - Lidhit, чтобы окружение встало в туже папку. Используем venv. Можно virtualenv - он позволяет выбрать версию python, pip при инициализации виртуального окружения.

`yourPC:~$ python3 -m venv Lidhit`

### Шаг 4. Активируем виртуальное окружением

```
yourPC:~$ source Lidhit/bin/activate
(Lidhit) yourPC:~$
```

### Шаг 5. Устанавливаем зависимости в виртуальном окружении (их можно будет увидеть в папке site-packages):

```
((Lidhit) yourPC:~$ cd Lidhit
(Lidhit) yourPC:~/Lidhit$ pip install -r requirements.txt
Collecting pip==21.1.3
  Downloading pip-21.1.3-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 729 kB/s
...
Successfully installed Flask-2.0.1 Jinja2-3.0.1 MarkupSafe-2.0.1 Werkzeug-2.0.1 attrs-21.2.0 certifi-2021.5.30 charset-normalizer-2.0.3 click-8.0.1 idna-3.2 itsdangerous-2.0.1 jsonschema-3.2.0 pip-21.1.3 pyrsistent-0.18.0 requests-2.26.0 setuptools-57.4.0 six-1.16.0 tinydb-4.5.1 urllib3-1.26.6 zipp-3.5.0
```

### Шаг 6. Запускаем сервер (development вариант, встроенный). В Win set необходимо использовать:

```
(Lidhit) yourPC:~/Lidhit$ export FLASK_APP=lidhit
(Lidhit) yourPC:~/Lidhit$ flask run
```

Результат:

*  Serving Flask app 'lidhit' (lazy loading)
  Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
  Debug mode: off
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)*

Для того, чтобы убедиться, что сервер отвечает, любым REST Client направляем запрос (пример для Visual Studio Code). Входные данные для веб-приложения:
список полей со значениями в теле POST запроса.

```
POST   http://127.0.0.1:5000/get_form
Content-Type: application/json

{
    "user_phone":"+7 926 200 15 17",
    "user_email":"petya@go.ru",
    "subjects": "text",
    "order_date":"2021-07-23"
}
```

Выходные данные: имя наиболее подходящей данному списку полей формы. При отсутствии совпадений с известными формами производится типизацию полей на лету и возвращается список полей с их типами:

```
{
  "status": "OK",
  "template_name": "Bank Account"
}
```

### Шаг 7. Проверка работы тестового скрипта. Запускаем второй терминал:

```
yourPC:~$ source Lidhit/bin/activate
(Lidhit) yourPC:~$ cd Lidhit
```

### Шаг 8. Запускаем тестовый скрипт. В качестве аргумента передаем файл с формой: dict список названий полей (key) и значений полей (value)/
Пример содержимого файла:
`{"user_phone":"+7 926 200 15 17","user_email":"petya@go.ru","subjects":"text","order_date":"2021-07-23"}`

Запускаем скрипт:
```
(Lidhit) yourPC:~/Lidhit$ python test_req.py test_payload.txt
{"status":"OK","template_name":"Bank Account"}
```

### Шаг 9. Останавливаем сервер (Ctrl+C) и деактивируем виртуальное окружение
`^C(Lidhit)yourPC:~/Lidhit$ deactivate`

### Шаг 10. Запуск проекта в IDE Pycharm
Нужно открыть папку проекта и, выбрав существующее окружение, настроить (добавить) Python Interpreter.
