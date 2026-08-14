print("=== Профиль Python-разработчика ===")

name = input("Введите имя: ").strip().title()
city = input("Введите город: ").strip().title()
favorite_topic = input("Любимая тема Python: ").strip()

try:
    projects_count = int(input("Сколько проектов вы создали? "))

    print()
    print("----- Профиль -----")
    print(f"Имя: {name}")
    print(f"Город: {city}")
    print(f"Количество проектов: {projects_count}")
    print(f"Любимая тема: {favorite_topic}")
    print("-------------------")
    print()

    if projects_count == 0:
        print("Первый проект уже скоро появится!")
    elif projects_count <= 3:
        print("Ты уже создал(а) несколько проектов — впереди backend-разработка!")
    else:
        print("Отличный опыт! Пора осваивать инструменты профессионального разработчика.")

except ValueError:
    print("Ошибка: количество проектов нужно вводить цифрами.")