def show_games(games):
    print("=== Каталог настольных игр ===")
    print()

    for number, game in enumerate(games, start=1):
        print(f"{number}. {game['name']}")
        print(f"   Жанр: {game['genre']}")
        print(f"   Игроков: {game['players']}")
        print()

def filter_by_genre(games, genre):
    filtered_games = []

    for game in games:
        if game["genre"].lower() == genre.lower():
            filtered_games.append(game)

    return filtered_games
