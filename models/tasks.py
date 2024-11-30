import json

TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, id, title, description, done=False, priority="Средний", due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def load_tasks(self):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def new_task(self):
        tasks = self.load_tasks()
        tasks.append({
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date
        })
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        print('Задача сохранена')

    def all_tasks(self):
        tasks = self.load_tasks()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("Нет задач.")

    def task_is_done(self, id):
        tasks = self.load_tasks()
        for task in tasks:
            if task['id'] == id:
                task['done'] = True
                break
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        print(f'Задача с ID {id} помечена как выполненная.')

    def edit_task(self, id, title=None, description=None, done=None, priority=None, due_date=None):
        tasks = self.load_tasks()
        for task in tasks:
            if task['id'] == id:
                if title is not None:
                    task['title'] = title
                if description is not None:
                    task['description'] = description
                if done is not None:
                    task['done'] = done
                if priority is not None:
                    task['priority'] = priority
                if due_date is not None:
                    task['due_date'] = due_date
                break
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        print(f'Задача с ID {id} обновлена.')

    def del_task(self, id):
        tasks = self.load_tasks()
        tasks = [task for task in tasks if task['id'] != id]
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        print(f'Задача с ID {id} удалена.')

    def import_task_to_csv(self, csv_file):
        tasks = self.load_tasks()
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Description", "Done", "Priority", "Due Date"])
            for task in tasks:
                writer.writerow([task['id'], task['title'], task['description'], task['done'], task['priority'],
                                 task['due_date']])
        print("Задачи экспортированы в CSV-файл.")

    def export_task_to_csv(self, csv_file):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    print(
                        f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}, Done: {row[3]}, Priority: {row[4]}, Due Date: {row[5]}")
        except FileNotFoundError:
            print("CSV-файл не найден.")


task1 = Task(1, "Первая задача", "Описание первой задачи.")
task1.new_task()
task2 = Task(2, "Вторая задача", "Описание второй задачи.", priority = 'Сложный')
task2.new_task()
task1.all_tasks()
task1.task_is_done(1)
task1.edit_task(1, description="Обновленное описание первой задачи.")
task1.all_tasks()
task1.del_task(2)
task1.del_task(1)
task1.del_task(1)
task1.all_tasks()




