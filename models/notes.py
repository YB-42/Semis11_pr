import json
import csv
from datetime import datetime

NOTES_FILE = "notes.json"

class Note:
    def __init__(self, id, title, content, timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def load_notes(self):
        try:
            with open(NOTES_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def new_note(self):
        notes = self.load_notes()
        notes.append({
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp
        })
        with open(NOTES_FILE, 'w') as file:
            json.dump(notes, file, indent=4)
        print('Заметка сохранена.')

    def see_all_notes(self):
        notes = self.load_notes()
        if notes:
            for note in notes:
                print(note)
        else:
            print("Нет заметок.")

    def info_note(self, id):
        notes = self.load_notes()
        for note in notes:
            if note['id'] == id:
                return note
        return None

    def change_note(self, id, title=None, content=None):
        notes = self.load_notes()
        for note in notes:
            if note['id'] == id:
                if title:
                    note['title'] = title
                if content:
                    note['content'] = content
                note['timestamp'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                break
        with open(NOTES_FILE, 'w') as file:
            json.dump(notes, file, indent=4)
        print('Заметка обновлена.')

    def del_info(self, id):
        notes = self.load_notes()
        notes = [note for note in notes if note['id'] != id]
        with open(NOTES_FILE, 'w') as file:
            json.dump(notes, file, indent=4)
        print("Заметка удалена.")

    def import_to_csv(self, csv_file):
        notes = self.load_notes()
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Content", "Timestamp"])
            for note in notes:
                writer.writerow([note['id'], note['title'], note['content'], note['timestamp']])
        print("Заметки экспортированы в CSV-файл.")

    def export_from_csv(self, csv_file):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    print(f"ID: {row[0]}, Title: {row[1]}, Content: {row[2]}, Timestamp: {row[3]}")
        except FileNotFoundError:
            print("CSV-файл не найден.")


