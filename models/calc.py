def calculator():
    print("Калькулятор")
    while True:
        try:
            expression = input("Введите пример (для выхода: выход): ")
            if expression.lower() == 'выход':
                print("Удачи!")
                break
            result = eval(expression)
            print(f"Результат: {result}")
        except ZeroDivisionError:
            print("Деление на ноль подумайте еще раз")
        except Exception as e:
            print(f"Некоректный ввод попробуйте еще раз")

if __name__ == "__main__":
    calculator()
