def import_data(data):
    with open('phonebook.csv', 'a+') as file:
        file.write(','.join(data))
        file.write(f"\n")