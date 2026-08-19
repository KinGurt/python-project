def show_tasks(tasks):
    print("=== Список задач ===")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")