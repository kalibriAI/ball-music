import pandas as pd

# Ваш JSON-данные (например, список песен)
data = [
    {"name": "Song 1", "author": "Billy Eylish"},
    {"name": "Song 2", "author": "Adele"},
    {"name": "Song 3", "author": "Ed Sheeran"}
]

# Преобразуем список JSON в DataFrame
df = pd.DataFrame(data)

# Сохраняем DataFrame в Excel-файл
df.to_excel("songs.xlsx", index=False, header=["Имя песни", "Автор"])
print("Excel файл успешно создан: songs.xlsx")
