from import_data import import_data
from export_data import export_data
from print_data import print_data
import random


def input_data():
    ID = str(random.randint(0,100))
    name = input("Введите фамилию: ")
    surname = input("Введите имя: ")
    phone = input("Введите телефон: ")
    comment = input("Введите описание контакта: ")
    return [ID, name, surname, phone, comment]


def action_choice():
    is_Ok = False
    while not is_Ok:
        print("Выберите действие:\n\
        1 - импорт;\n\
        2 - экспорт;")
        num = input("Введите цифру: ")
        if num == '1':
            import_data(input_data())
            data = export_data()
            print_data(data)
            is_Ok = True
        elif num == '2':
            data = export_data()
            print_data(data)
            is_Ok = True
        else:
            print("Неверный ввод, попробуйте ещё раз")