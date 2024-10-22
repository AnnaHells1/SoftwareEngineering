import csv
import os
import datetime

def create_expenses_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Дата', 'Сумма', 'Трата'])

def add_expense(file_name, amount, expense):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_name, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, expense])

def display_expenses(file_name):
    with open(file_name, 'r', encoding='cp1251', errors='replace') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def main():
    expenses_file = "expenses.csv"

    if not os.path.isfile(expenses_file):
        create_expenses_file(expenses_file)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить расход")
        print("2. Просмотреть расходы")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = input("Введите сумму расхода: ")
            expense = input("Введите трать: ")
            add_expense(expenses_file, amount, expense)
            print("Расход успешно добавлен!")

        elif choice == "2":
            display_expenses(expenses_file)

        elif choice == "3":
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")

if __name__ == "__main__":
    main()