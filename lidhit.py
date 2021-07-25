from flask import Flask
from tinydb import TinyDB, Query
from flask import request, jsonify
from validation import replacing_value_with_type

app = Flask(__name__)

db = TinyDB('db/db.json')

@app.route("/db_all")
def all_db_rec():
    """
    Вывод содержимого базы данных
    :return:
    """
    text=str(db.all())
    return f"<p>{text}</p>"

@app.route('/get_form', methods=['POST', ])
def get_form():
    """
    Получаем имя шаблона. Полей в пришедшей форме может быть больше чем в шаблоне,
    в этом случае шаблон все равно будет считаться подходящим
    :return:
    """

    # request.json: parsed JSON data. The request must have the application/json content type,
    # or use request.get_json(force=True) to ignore the content type.
    # проверка: есть ли json
    try:
        req_data = request.get_json(force=True)
    except:
        return jsonify({'status': 'Wrong request!'})

    # Валидируем и одновременно заменяем значения полей на типы
    new_data=replacing_value_with_type(req_data)
    if len(new_data) == 0:
        return jsonify({'status': 'Wrong request!'})

    # Ищем имя шаблона во всех документах БД
    for db_item in db:
        # очередной документ
        is_searched=True
        result=''
        # по всем полям кроме "name"
        for nk, nv in db_item.items():
            if nk == 'name':
                result=nv
                continue
            if new_data.get(nk) == nv:
                continue
            else:
                is_searched = False
        if is_searched:
            return jsonify({'status': 'OK', 'template_name': result})

    return jsonify({'status': 'OK', 'outcome_ison': new_data})

@app.route('/get_form_strong', methods=['POST', ])
def get_form_strong():
    """
    Строгое соответствие полям в присланной форме
    :return:
    """

    # request.json: parsed JSON data. The request must have the application/json content type,
    # or use request.get_json(force=True) to ignore the content type.
    # проверка: есть ли json
    try:
        req_data = request.get_json(force=True)
    except:
        return jsonify({'status': 'Wrong request!'})

    # Заменяем значения на типы полей
    new_data=replacing_value_with_type(req_data)
    if len(new_data) == 0:
        return jsonify({'status': 'Wrong request!'})

    # ищем нужный фрагмент
    result=db.search(Query().fragment(new_data))

    # проверка результата поиска
    if result != []:
        return jsonify({'status': 'OK', 'template_name': result[0]['name']})
    else:
        return jsonify({'status': 'OK', 'outcome_ison': new_data})



