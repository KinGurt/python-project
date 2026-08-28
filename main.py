from games import *

games = [
   {
       "name": "Каркассон",
       "genre": "Стратегия",
       "players": "2–5",
   },
   {
       "name": "Диксит",
       "genre": "Воображение",
       "players": "3–6",
   },
   {
       "name": "Билет на поезд",
       "genre": "Стратегия",
       "players": "2–5",
   },
]

show_games(games)

genre = input("Введите жанр для поиска: ").strip()

filtered_games = filter_by_genre(games, genre)

print()

if filtered_games:
    show_games(filtered_games)
else:
    print("Игры такого жанра не найдены.")

