import json
import csv

CONTACTS_FILE = 'contacts.json'

class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def load_contacts(self):
        try:
            with open(CONTACTS_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def new_cont(self):
        contacts = self.load_contacts()
        contacts.append({
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        })
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
        print('Контакт сохранен')

    def find_contact(self, name, phone=None):
        contacts = self.load_contacts()
        for contact in contacts:
            if contact['name'] == name and (phone is None or contact['phone'] == phone):
                return contact
        return None

    def edit_contact(self, id, name=None, phone=None, email=None):
        contacts = self.load_contacts()
        for contact in contacts:
            if contact['id'] == id:
                if name is not None:
                    contact['name'] = name
                if phone is not None:
                    contact['phone'] = phone
                if email is not None:
                    contact['email'] = email
                break
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
        print(f'Контакт с ID {id} обновлен')

    def del_contact(self, id):
        contacts = self.load_contacts()
        contacts = [contact for contact in contacts if contact['id'] != id]
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
        print(f'Контакт с ID {id} удален')

    def import_cont_to_csv(self, csv_file):
        contacts = self.load_contacts()
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Phone", "Email"])
            for contact in contacts:
                writer.writerow([contact['id'], contact['name'], contact['phone'], contact['email']])
        print("Контакты экспортированы в CSV-файл")

    def export_to_csv(self, csv_file):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
        except FileNotFoundError:
            print("CSV-файл не найден")

contact1 = Contact(1, "Иван Иванов", "+123456789", "ivan@example.com")
contact1.new_cont()
contact2 = Contact(2, "Петр Петров", "+987654321", "petr@example.com")
contact2.new_cont()

found_contact = contact1.find_contact("Иван Иванов")
print(found_contact)

contact1.edit_contact(1, phone="+111111111")
contact1.del_contact(2)
contact1.del_contact(1)
contact1.del_contact(1)

contact1.import_cont_to_csv("contacts.csv")
contact1.export_to_csv("contacts.csv")