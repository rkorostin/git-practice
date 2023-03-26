def export_data():
    with open('phonebook.csv', 'r') as file:
        data = []
        for line in file:
            data.append(line.strip().split(','))
    return data