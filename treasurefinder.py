import csv

# data = (('55', '14', '25', '52', '21'),
#         ('44', '31', '11', '53', '43'),
#         ('24', '13', '45', '12', '34'),
#         ('42', '22', '43', '32', '41'),
#         ('51', '23', '33', '54', '15'))

# Not sure about requirement "Your program must first read in the treasure map data into a 5 by 5"
# so I suppose that data is stored in csv file


def csv_to_array(file):
    with open(file) as f:
        reader = csv.reader(f)
        return list(reader)


def treasure_finder(input_data):
    counter = 1
    row, column = 0, 0
    result = ''

    def validator(input_data):
        nonlocal counter, row, column, result
        element = input_data[row][column]

        if counter == 25:
            result = 'Unfortunately there is no treasure here'
            return
        if element[0] == str(row+1) and element[1] == str(column+1):
            result = f"You've found treasure in the cell {element}"
            return

        counter += 1
        row, column = (int(i)-1 for i in element)
        validator(input_data)
    validator(input_data)
    return result


if __name__ == '__main__':
    data = csv_to_array('test.csv')
    print(treasure_finder(data))
