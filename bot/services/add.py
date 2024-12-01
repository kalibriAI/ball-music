import json


def save_to_json(data, filename="songs.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

