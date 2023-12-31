import csv
import os

def show_menu():
    print("\nВыберите необходимое действие:")
    print("1. Отобразить весь справочник")
    print("2. Найти абонента по фамилии")
    print("3. Найти абонента по номеру телефона")
    print("4. Добавить абонента в справочник")
    print("5. Изменить данные абонента")
    print("6. Удалить абонента из справочника")
    print("7. Закончить работу")
    choice = int(input())
    return choice

def print_phonebook(phonebook):
    for entry in phonebook:
        print('|'.join(entry))

def search_by_name(phonebook, name):
    found_entries = [entry for entry in phonebook if entry[0].lower() == name.lower()]
    if found_entries:
        for entry in found_entries:
            print('|'.join(entry))
    else:
        print("Абонент не найден.")

def search_by_number(phonebook, number):
    found_entries = [entry for entry in phonebook if entry[2] == number]
    if found_entries:
        for entry in found_entries:
            print('|'.join(entry))
    else:
        print("Абонент не найден.")

def add_entry(phonebook):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    description = input("Введите примечание: ")
    entry = [last_name, first_name, phone_number, description]
    phonebook.append(entry)
    print("Абонент успешно добавлен.")

def update_entry(phonebook, name):
    found_entries = [index for index, entry in enumerate(phonebook) if entry[0].lower() == name.lower()]
    if found_entries:
        print(f"Найдено {len(found_entries)} записей с именем {name}.")
        for index in found_entries:
            entry = phonebook[index]
            print("Текущая информация:")
            print('|'.join(entry))
            print("Введите новые данные:")
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            phone_number = input("Номер телефона: ")
            description = input("Примечание: ")
            phonebook[index] = [last_name, first_name, phone_number, description]
            print("Данные успешно обновлены.")
    else:
        print("Абонент не найден.")

def delete_entry(phonebook, name):
    found_entries = [entry for entry in phonebook if entry[0].lower() == name.lower()]
    if found_entries:
        print(f"Найдено {len(found_entries)} записей с именем {name}.")
        confirm = input("Вы уверены, что хотите удалить эти записи? (y/n): ")
        if confirm.lower() == 'y':
            phonebook[:] = [entry for entry in phonebook if entry[0].lower() != name.lower()]
            print("Записи успешно удалены.")
        else:
            print("Удаление отменено.")
    else:
        print("Абонент не найден.")

def work_with_phonebook():
    choice = show_menu()

    if not os.path.isfile('phonebook.csv'):
        with open('phonebook.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Фамилия', 'Имя', 'Телефон', 'Описание'])
            print("Файл 'phonebook.csv' создан.")

    with open('phonebook.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        phonebook = list(reader)

    while choice != 7:
        if choice == 1:
            print_phonebook(phonebook)
        elif choice == 2:
            name = input("Введите фамилию для поиска: ")
            search_by_name(phonebook, name)
        elif choice == 3:
            number = input("Введите номер: ")
            search_by_number(phonebook, number)
        elif choice == 4:
            add_entry(phonebook)
            with open('phonebook.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(phonebook[-1])
        elif choice == 5:
            name = input("Введите фамилию для обновления данных: ")
            update_entry(phonebook, name)
            with open('phonebook.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(phonebook)
        elif choice == 6:
            name = input("Введите фамилию для удаления: ")
            delete_entry(phonebook, name)
            with open('phonebook.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(phonebook)
        elif choice > 7:
            print("Вы ввели слишком большое значение, попробуйте еще раз.")
        print()
        choice = show_menu()

work_with_phonebook()
