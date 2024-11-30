import json


def save_to_json(data, filename="songs.json"):
    try:
        # Если файл существует, загружаем существующие данные
        with open(filename, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        # Если файла нет, создаем пустой список
        existing_data = []

    # Добавляем новую запись в список
    existing_data.append(data)

    # Сохраняем данные обратно в файл
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

