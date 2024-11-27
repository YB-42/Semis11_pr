# finance.py
import json
import csv
from datetime import datetime

FINANCE_FILE = "finance.json"

class FinanceRecord:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        return FinanceRecord(
            data['id'],
            float(data['amount']),
            data['category'],
            data['date'],
            data['description']
        )

class FinanceManager:
    def __init__(self):
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(FINANCE_FILE, 'r') as file:
                return [FinanceRecord.from_dict(record) for record in json.load(file)]
        except FileNotFoundError:
            return []

    def save_records(self):
        with open(FINANCE_FILE, 'w') as file:
            json.dump([record.to_dict() for record in self.records], file, indent=4)

    def add_record(self, amount, category, date, description):
        new_id = max((record.id for record in self.records), default=0) + 1
        new_record = FinanceRecord(new_id, amount, category, date, description)
        self.records.append(new_record)
        self.save_records()
        print("Finance record added successfully.")

    def list_records(self):
        print("\nFinance Records:")
        for record in self.records:
            print(f"ID: {record.id}, Amount: {record.amount}, Category: {record.category}, "
                  f"Date: {record.date}, Description: {record.description}")

    def filter_records(self, by_category=None, by_date=None):
        filtered = self.records
        if by_category:
            filtered = [record for record in filtered if record.category == by_category]
        if by_date:
            filtered = [record for record in filtered if record.date == by_date]
        return filtered

    def generate_report(self, start_date=None, end_date=None):
        total_income = 0
        total_expense = 0

        for record in self.records:
            record_date = datetime.strptime(record.date, "%d-%m-%Y")
            if start_date and record_date < datetime.strptime(start_date, "%d-%m-%Y"):
                continue
            if end_date and record_date > datetime.strptime(end_date, "%d-%m-%Y"):
                continue
            if record.amount > 0:
                total_income += record.amount
            else:
                total_expense += record.amount

        print("\nFinance Report:")
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Net Balance: {total_income + total_expense}")

    def export_to_csv(self, file_name="finance.csv"):
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "amount", "category", "date", "description"])
            writer.writeheader()
            for record in self.records:
                writer.writerow(record.to_dict())
        print(f"Finance records exported to {file_name}.")

    def import_from_csv(self, file_name="finance.csv"):
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_record(float(row["amount"]), row["category"], row["date"], row["description"])
        print(f"Finance records imported from {file_name}.")
