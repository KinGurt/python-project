def show_games(games):
    print("=== Каталог настольных игр ===")
    print()

    for number, game in enumerate(games, start=1):
        print(f"{number}. {game['name']}")
        print(f"   Жанр: {game['genre']}")
        print(f"   Игроков: {game['players']}")
        print()

