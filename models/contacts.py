import json

CONTACTS_FILE = 'contacts.json'

class Contact:
    def __int__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "phone": self.phone,
                "email": self.email
                }
    def from_dict(data):
        return Contact(data['id'], data['name'], data['phone'], data['email'])

class ContactManager:
    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        with open(CONTACTS_FILE, 'r') as file:
            return [Contact.from_dict(contact) for contact in json.load(file)]
    def save_contacts(self):
        with open(CONTACTS_FILE, 'w') as fl:
            json.dump([contact.to_dict() for contact in self.contacts], fl, indent = 4)

    def add_contact(self, name, phone, email):
        new_id  = max((contact.id for contact in self.contacts), default=0)+1
        new_contact = Contact(new_id, name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print('Контакт добавлен')