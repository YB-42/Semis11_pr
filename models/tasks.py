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

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description,
                "done": self.done, "priority": self.priority, "due_date": self.due_date}

    def from_dict(data):
        return Task(data['id'], data['title'], data['description'],
                    data['done'], data['priority'], data['due_date'])

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
            with open(TASKS_FILE, 'r') as fl:
                return [Task.from_dict(task) for task in json.load(fl)]

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as fl:
            json.dump([task.to_dict() for task in self.tasks], fl, indent=4)

    def create_task(self, title, description, priority="Средний", due_date=None):
        new_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(new_id, title, description, priority=priority, due_date=due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        print("Задача создана")

    def list_tasks(self):
        for task in self.tasks:
            print(f"{task.id}. {task.title} | Важность: {task.priority} | Длительность: {task.due_date} | Выполнено: {task.done}")

    def mark_task_done(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.done = True
            self.save_tasks()
            print("Задача выполнена")
        else:
            print("Задача не найдена")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        print("Задача удалена")
