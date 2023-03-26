def print_data(data):
    if len(data):
        print("id".center(20),"Фамилия".center(20), "Имя".center(20),
              "Телефон".center(20), "Описание".center(20))
        print("*"*105)
        for item in data:
            print(item[0].center(20), item[1].center(20),
                  item[2].center(20), item[3].center(20), item[4].center(20))
    else:
        print("id".center(20), "Фамилия".center(20), "Имя".center(20),
              "Телефон".center(20), "Описание".center(20))
        print("*"*105)