def print_data(data, search = False):
    if len(data) > 0:
        print("id".center(5), "Фамилия".center(10), "Имя".center(7), "Класс".center(6), "Статус".center(6),\
           "Ряд".center(4), "Парта".center(6),\
            "Город".center(10), "Улица".center(8), "Дом".center(6), "Квартира".center(4), "Примечание".center(15))
        print("-"*100)
        if not search:
            del data[0]
        for item in data:
            print(item[0].center(5), item[1].center(10), item[2].center(7), item[3].center(6), item[4].center(6),\
            item[5].center(4), item[6].center(6),\
            item[7].center(7), item[8].center(8), item[9].center(6), item[10].center(4), item[11].center(15))
    else:
        print("\n")
        print("*"*50 + "\nСправочник пуст!\n" + "*"*50)
        print("\n")