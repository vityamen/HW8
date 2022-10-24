from write_data import count_data

def input_data():
    dict = dict()
    Id = count_data("name.csv") 
    dict["id"] = Id
    dict["surname"] = input('Введите фамилию: ')
    dict["name"] = input('Введите имя: ')
    dict["class"] = input('Введите класс: ')
    dict["status"] = input('Укажите успеваемость: ')
    dict["row"] = input('Введите номер ряда: ')
    dict["col"] = input('Введите Номер парты: ')
    dict["city"] = input('Введите Город: ')
    dict["street"] = input('Введите название улицы: ')
    dict["house"] = input('Введите номер дома: ')
    dict["apartament"] = input('Введите номер квартиры: ')
    dict["other"] = input('Введите комментарий: ')
    return dict