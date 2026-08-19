from tasks import *

project_tasks = [
    "Создать папку проекта",
    "Написать первую функцию",
    "Сделать первый коммит",
]

new_task = input("Введите новую задачу: ").strip()

if new_task:
    add_task(project_tasks, new_task)
else:
    print("Пустую задачу добавлять нельзя.")

show_tasks(project_tasks)


