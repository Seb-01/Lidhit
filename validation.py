import jsonschema
from schema import PHONE, DATE_DDMMYYYY_slash, DATE_YYYYMMDD_dash, TEXT, EMAIL

def chek_type_of_field(field_value, schema):
    """
    Валидирует и возвоащает тип поля, либо "bad_format"
    :param field_value:
    :return:
    """
    try:
        jsonschema.validate(field_value, schema=schema)
        return True
    except:
        return False

def replacing_value_with_type(req_data :dict):
    """
    Заменяет значение на типы
    :return:
    """
    new_data = {}
    for k, v in req_data.items():
        # 1. Date?
        if chek_type_of_field(v, DATE_DDMMYYYY_slash) or chek_type_of_field(v, DATE_YYYYMMDD_dash):
            new_data[k] = "date"
        # 2. Phone?
        elif chek_type_of_field(v, PHONE):
            new_data[k] = "phone"
        # 3. Email?
        elif chek_type_of_field(v, EMAIL):
            new_data[k] = "email"
        # 4. Just a text?
        elif chek_type_of_field(v, TEXT):
            new_data[k] = "text"
        else:
            new_data.clear()
            return new_data

    return new_data