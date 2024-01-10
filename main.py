"""
ToDoList Application

Manage tasks and subtasks in a JSON file.

Author: Bratchik Oleg
Date: 29-12-2023
"""

import json
from datetime import date

# Що обов’язково має включати проєкт (10 балів):
# [] Можливість додавати/видаляти задачі
# [] Можливість позначати задачу як виконану
# [] Задачі з дедлайнами, можливість змінювати дедлайн
# [] Можливість додавати підзадачі


# [] Можливість роботи з різними файлами за назвою файла
# [] Зберігання в файл, щоб після перезапуску програми задачі зберігалися
class ToDoList:

    def __init__(self, filename='lists/tasks.json'):
        self.filename = filename
        self.list_data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
                return tasks
        except FileNotFoundError:
            return []

    def add_tasks(self, task_title, deadline):
        new_data = dict(title=task_title, timestamp='', deadline=deadline, status=False, subtasks=[])
        self.list_data.append(new_data)
        self.save_to_file()

    def delete_task(self, task_title):
        self.list_data = [item for item in self.list_data if task_title not in item]

    def add_subtasks(self,index, subtask_title):
        if 0 <= index < len(self.list_data):
            subtasks = dict(subtitle= subtask_title, timestamp='', deadline='', status=False)
            self.list_data[index]['subtasks'].append(subtasks)
            self.save_to_file()

    def mark_as_done(self, index):
        if 0 <= index < len(self.list_data):
            task_status = self.list_data [index].get('status')
            self.list_data[index]['status'] = not task_status
            # Change all subtask status
            subtasks = self.list_data[0]['subtasks']
            for subtask in subtasks:
                subtasks[subtask]['status'] = not task_status

    def change_deadline(self, index, new_deadline):
        if 0 <= index < len(self.list_data):
            self.list_data[index]['deadline'] = new_deadline

    def json_serializable(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.list_data, file, default=self.json_serializable, indent=4)

    def print_tasks(self):
        for i, task in enumerate(self.list_data):
            print(f"{i + 1}. {task ['title']}")
            if task['deadline']:
                print(f"   Deadline: {task ['deadline']}")
            if task['subtasks']:
                print("   Subtasks:")
                for subtask in task ['subtasks']:
                    print(f"      - [{'x' if subtask ['done'] else ' '}] {subtask ['title']}")
            print()


# t = ToDoList()

# t.add_tasks('Some another task', '2024-01-29')
# t.add_subtasks(0, 'Some  task')
# print(t.list_data)
# t.add_subtasks(0, 'Some adasfsf task')
# # t.save_to_file()
# # t.list_data
# print(t.list_data)
