from push_data import *
from read_data import *
from print_data import *
from search_data import *

def start():
    print("Выберете вариант работы с базой данных:\n\
    1 - Вывести всю информацию об учениках, содержащуюся в БД;\n\
    2 - Добавить ученика в БД;\n\
    3 - Найти ученика в БД;\n\
    4 - Выход.")
    ch = input("Введите цифру: ")
    while True:
        if ch == '1':
            data = read_data()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены!")                
            start()
        elif ch == '4':
            print("Работа с БД окончена. До свидания!")
            break
        else:
            print("Введите корректную цифру!")
            start()