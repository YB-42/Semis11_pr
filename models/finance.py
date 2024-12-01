import json
import csv
from datetime import datetime

FINANCE_FILE = "finance.json"

class FinanceRecord:
    def __init__(self, id, amount, category, date=None, description=""):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.description = description

    def load_records(self):
        try:
            with open(FINANCE_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_record(self):
        records = self.load_records()
        records.append({
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        })
        with open(FINANCE_FILE, 'w') as file:
            json.dump(records, file, indent=4)
        print('Фин. запись добавлена')

    def view_records(self, start_date=None, end_date=None, category=None):
        records = self.load_records()
        filtered_records = []

        for record in records:
            record_date = datetime.strptime(record['date'], "%Y-%m-%d")
            if (start_date is None or record_date >= start_date) and \
               (end_date is None or record_date <= end_date) and \
               (category is None or record['category'] == category):
                filtered_records.append(record)

        for record in filtered_records:
            print(record)

    def generate_report(self, start_date, end_date):
        records = self.load_records()
        total_income = 0
        total_expense = 0

        for record in records:
            record_date = datetime.strptime(record['date'], "%Y-%m-%d")
            if start_date <= record_date <= end_date:
                if record['amount'] > 0:
                    total_income += record['amount']
                else:
                    total_expense += record['amount']

        print(f"Общий доход: {total_income}")
        print(f"Общий расход: {total_expense}")
        print(f"Чистый доход: {total_income + total_expense}")

    def del_record(self, id):
        records = self.load_records()
        records = [record for record in records if record['id'] != id]
        with open(FINANCE_FILE, 'w') as file:
            json.dump(records, file, indent=4)
        print(f'Запись с ID {id} удален')

    def import_from_csv(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = FinanceRecord(
                    id=int(row['ID']),
                    amount=float(row['Amount']),
                    category=row['Category'],
                    date=row['Date'],
                    description=row['Description']
                )
                record.add_record()
        print("Фин. записи импортированы из CSV")

    def export_to_csv(self, csv_file):
        records = self.load_records()
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Amount", "Category", "Date", "Description"])
            for record in records:
                writer.writerow([record['id'], record['amount'], record['category'], record['date'], record['description']])
        print("Фин. записи экспортированы в CSV")


record1 = FinanceRecord(1, 1000, "Доход", "2023-10-01", "Зарплата")
record1.add_record()
record2 = FinanceRecord(2, -200, "Расход", "2023-10-02", "Покупка продуктов")
record2.add_record()

print("Все записи:")
record1.view_records()

print("\nЗаписи с 2023-10-01 по 2023-10-02:")
record1.view_records(datetime(2023, 10, 1), datetime(2023, 10, 2))

print("\nОтчет за период с 2023-10-01 по 2023-10-02:")
record1.generate_report(datetime(2023, 10, 1), datetime(2023, 10, 2))

record1.export_to_csv("finance_records.csv")
record1.import_from_csv("finance_records.csv")