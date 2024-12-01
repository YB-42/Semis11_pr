from datetime import datetime

from finance import FinanceRecord
from tasks import Task
from notes import Note
from contacts import Contact


def main_menu():
    print("Главное меню")
    print("  Добро пожаловать в Персональный помощник!")
    print("  Выберите действие:")
    print("  1. Управление заметками")
    print("  2. Управление задачами")
    print("  3. Управление контактами")
    print("  4. Управление финансовыми записями")
    print("  5. Калькулятор")
    print("  6. Выход")


def task_menu():
    print(" Управление задачами:")
    print(" 1. Добавить новую задачу")
    print(" 2. Просмотреть задачи")
    print(" 3. Отметить задачу как выполненную")
    print(" 4. Редактировать задачу")
    print(" 5. Удалить задачу")
    print(" 6. Экспорт задач в CSV")
    print(" 7. Импорт задач из CSV")
    print(" 8. Назад")


def note_menu():
    print(" Управление заметками:")
    print(" 1. Добавить новую заметку")
    print(" 2. Просмотреть все заметки")
    print(" 3. Изменить заметку")
    print(" 4. Удалить заметку")
    print(" 5. Экспорт заметок в CSV")
    print(" 6. Импорт заметок из CSV")
    print(" 7. Назад")


def contact_menu():
    print(" Управление контактами:")
    print(" 1. Добавить новый контакт")
    print(" 2. Просмотреть все контакты")
    print(" 3. Изменить контакт")
    print(" 4. Удалить контакт")
    print(" 5. Экспорт контактов в CSV")
    print(" 6. Импорт контактов из CSV")
    print(" 7. Назад")

def finance_menu():
    print("""Управление финансовыми записями:
 1. Добавить новую запись
 2. Просмотреть все записи
 3. Генерация отчёта
 4. Удалить запись
 5. Экспорт финансовых записей в CSV
 6. Импорт финансовых записей из CSV
 7. Назад""")



def main():
    task_manager = Task(0, "", "")
    note_manager = Note(0, "", "")
    contact_manager = Contact(0, "", "", "")
    finance_manager = FinanceRecord(0, 0, "", "", "")

    while True:
        main_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            while True:
                note_menu()
                note_choice = input("Выберите действие: ")

                if note_choice == '1':
                    title = input("Введите название заметки: ")
                    content = input("Введите содержание заметки: ")
                    new_note = Note(id=len(note_manager.load_notes()) + 1, title=title, content=content)
                    new_note.new_note()
                    print("Заметка успешно добавлена!")

                elif note_choice == '2':
                    print("Список заметок:")
                    note_manager.see_all_notes()

                elif note_choice == '3':
                    note_id = int(input("Введите ID заметки, которую хотите изменить: "))
                    title = input("Введите новое название заметки (или оставьте пустым для пропуска): ")
                    content = input("Введите новое содержание заметки (или оставьте пустым для пропуска): ")
                    note_manager.change_note(note_id, title if title else None, content if content else None)

                elif note_choice == '4':
                    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
                    note_manager.del_info(note_id)

                elif note_choice == '5':
                    csv_file = input("Введите имя CSV-файла для экспорта: ")
                    note_manager.import_to_csv(csv_file)

                elif note_choice == '6':
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    note_manager.export_from_csv(csv_file)

                elif note_choice == '7':
                    break
                else:
                    print("Неверный выбор. Пожалуйста, попробуйте снова.")

        elif choice == '2':
            while True:
                task_menu()
                task_choice = input("Выберите действие: ")

                if task_choice == '1':
                    title = input("Введите название задачи: ")
                    description = input("")

                elif task_choice == '2':
                    print("Список задач:")
                    task_manager.all_tasks()

                elif task_choice == '3':
                    task_id = int(input("Введите ID задачи, которую хотите отметить как выполненную: "))
                    task_manager.task_is_done(task_id)

                elif task_choice == '4':
                    task_id = int(input("Введите ID задачи, которую хотите редактировать: "))
                    title = input("Введите новое название задачи (или оставьте пустым для пропуска): ")
                    description = input("Введите новое описание задачи (или оставьте пустым для пропуска): ")
                    priority = input("Введите новый приоритет (или оставьте пустым для пропуска): ")
                    due_date = input("Введите новую дату выполнения (или оставьте пустым для пропуска): ")
                    task_manager.edit_task(task_id, title if title else None, description if description else None,
                                       None, priority if priority else None, due_date if due_date else None)

                elif task_choice == '5':
                    task_id = int(input("Введите ID задачи, которую хотите удалить: "))
                    task_manager.del_task(task_id)

                elif task_choice == '6':
                    csv_file = input("Введите имя CSV-файла для экспорта: ")
                    task_manager.export_task_to_csv(csv_file)

                elif task_choice == '7':
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    task_manager.import_task_to_csv(csv_file)

                elif task_choice == '8':
                    break
                else:
                    print("Неверный выбор. Пожалуйста, попробуйте снова.")

        elif choice == '3':
            while True:
                contact_menu()
                contact_choice = input("Выберите действие: ")

                if contact_choice == '1':
                    name = input("Введите имя контакта: ")
                    phone = input("Введите номер телефона: ")
                    email = input("Введите адрес электронной почты: ")
                    new_contact = Contact(id=len(contact_manager.load_contacts()) + 1, name=name, phone=phone,
                                          email=email)
                    new_contact.new_cont()
                    print("Контакт успешно добавлен!")

                elif contact_choice == '2':
                    print("Список контактов:")
                    contacts = contact_manager.load_contacts()
                    if contacts:
                        for contact in contacts:
                            print(contact)
                    else:
                        print("Нет контактов.")

                elif contact_choice == '3':
                    contact_id = int(input("Введите ID контакта, который хотите изменить: "))
                    name = input("Введите новое имя контакта (или оставьте пустым для пропуска): ")
                    phone = input("Введите новый номер телефона (или оставьте пустым для пропуска): ")
                    email = input("Введите новый адрес электронной почты (или оставьте пустым для пропуска): ")

                    contact_manager.edit_contact(contact_id, name if name else None, phone if phone else None,
                                                 email if email else None)

                elif contact_choice == '4':
                    contact_id = int(input("Введите ID контакта, который хотите удалить: "))
                    contact_manager.del_contact(contact_id)

                elif contact_choice == '5':
                    csv_file = input("Введите имя CSV-файла для экспорта: ")
                    contact_manager.import_cont_to_csv(csv_file)

                elif contact_choice == '6':
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    contact_manager.export_to_csv(csv_file)

                elif contact_choice == '7':
                    break
                else:
                    print("Неверный выбор. Пожалуйста, попробуйте снова.")



        elif choice == '4':
            while True:
                finance_menu()
                finance_choice = input("Выберите действие: ")
                if finance_choice == "1":
                    amount = float(input("Введите сумму: "))
                    category = input("Введите категорию: ")
                    date = input("Введите дату (в формате ГГГГ-ММ-ДД, оставьте пустым для текущей даты): ")
                    description = input("Введите описание (необязательно): ")
                    if not date:
                        date = None
                    new_record = FinanceRecord(id=len(finance_manager.load_records()) + 1, amount=amount,
                                               category=category, date=date, description=description)
                    new_record.add_record()
                    print("Финансовая запись успешно добавлена!")

                elif finance_choice == "2":
                    print("Список финансовых записей:")
                    start_date_input = input(
                        "Введите начальную дату (или оставьте пустым для всех записей, формат ГГГГ-ММ-ДД): ")
                    end_date_input = input(
                        "Введите конечную дату (или оставьте пустым для всех записей, формат ГГГГ-ММ-ДД): ")
                    start_date = datetime.strptime(start_date_input, "%Y-%m-%d") if start_date_input else None
                    end_date = datetime.strptime(end_date_input, "%Y-%m-%d") if end_date_input else None
                    category = input("Введите категорию для фильтрации (или оставьте пустым для всех): ") or None
                    finance_manager.view_records(start_date=start_date, end_date=end_date, category=category)

                elif finance_choice == "3":
                    #generate_report
                    start_date_input = input(
                        "Введите начальную дату (или оставьте пустым для всех записей, формат ГГГГ-ММ-ДД): ")
                    end_date_input = input(
                        "Введите конечную дату (или оставьте пустым для всех записей, формат ГГГГ-ММ-ДД): ")
                    start_date = datetime.strptime(start_date_input, "%Y-%m-%d") if start_date_input else None
                    end_date = datetime.strptime(end_date_input, "%Y-%m-%d") if end_date_input else None
                    finance_manager.generate_report(start_date, end_date)


                elif finance_choice == "4":
                    record_id = int(input("Введите ID записи, которую хотите удалить: "))
                    finance_manager.del_record(record_id)

                elif finance_choice == "5":
                    csv_file = input("Введите имя CSV-файла для экспорта: ")
                    finance_manager.export_to_csv(csv_file)

                elif finance_choice == "6":
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    finance_manager.import_from_csv(csv_file)

                elif finance_choice == "7":
                    break
                else:
                    print("Неверный выбор. Пожалуйста, попробуйте снова.")


        elif choice == '5':
            print("Калькулятор")
            while True:
                try:
                    expression = input("Введите пример (для выхода: выход): ")
                    if expression.lower() == 'выход':
                        print("Удачи!")
                        break
                    result = eval(expression)
                    # eval - комана которая позволяет считаь вырадение написанное в виде строки и выводить результат в виде числа что удобно для облегчения кода
                    print(f"Результат: {result}")
                except ZeroDivisionError:
                    print("Деление на ноль подумайте еще раз")
                except Exception as e:
                    print(f"Некоректный ввод попробуйте еще раз")

        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()