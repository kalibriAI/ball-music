import pandas as pd
from json import load


def make_excel(aid: int):
    with open('songs.json', 'r', encoding='utf-8') as file:
        data = load(file)

    df = pd.DataFrame(data)
    df.to_excel("songs.xlsx", index=False, header=["Отправитель", "Название песни", "Автор"])
