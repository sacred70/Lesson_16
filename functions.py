import json

def read_json(file) -> list:
    """
    Функция читает данные из .json файла
    """
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)

    return json_data