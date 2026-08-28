def show_tasks(tasks):
    print("=== Список задач ===")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

def add_task(tasks, task_name):
    tasks.append(task_name)
    print(f"Задача добавлена: {task_name}")
