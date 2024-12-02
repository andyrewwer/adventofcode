import sys

basic_file_name = 'input-basic.csv' if len(sys.argv) < 2 else sys.argv[1]
expected = 467835

full_file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]


def isSurroundedBySymbol(data, y, x_start, x_end):
    y_min = 0 if y == 0 else y - 1
    y_max = y if y == len(data) - 1 else y + 1
    x_min = 0 if x_start == 0 else x_start - 1
    x_max = x_end if x_end == len(data[y]) - 1 else x_end + 1

    # print('y_min', y_min, 'y', y, 'y_max', y_max, 'len(data)', len(data), 'len(data[y])', len(data[y]))
    # print('x_min', x_min, 'x', 'x_max', x_max)
    # print(y_min, y, y_max, len(data))
    for i in range(y_min, y_max+1):
        for j in range(x_min, x_max+1):
            if not data[i][j].isnumeric() and data[i][j] != '.':
                return True
    return False

def isSurroundedByNumbers(data, y, x):
    y_min = 0 if y == 0 else y - 1
    y_max = y if y == len(data) - 1 else y + 1
    x_min = 0 if x == 0 else x - 1
    x_max = x if x == len(data[y]) - 1 else x + 1

    # print('y_min', y_min, 'y', y, 'y_max', y_max, 'len(data)', len(data), 'len(data[y])', len(data[y]))
    # print('x_min', x_min, 'x', 'x_max', x_max)
    # print(y_min, y, y_max, len(data))
    count = 0
    for i in range(y_min, y_max+1):
        for j in range(x_min, x_max+1):
            if data[i][j].isnumeric():
                count += 1
    
    print(count)
    #how to tell if they are the same number
    return count == 2

def findSurroundingNumbers(data, x, y):
    pass

def main(file_name, expected=0):
    with open(file_name) as file:
        sum = 0
        data = file.read().splitlines()
        x_start = -1
        number = ''
        for y in range(0, len(data)):
            for x in range(0, len(data[y])):
                if data[y][x] == "*":
                    print(isSurroundedByNumbers(data, y, x))
                # print('y', y, 'x', x, 'data[y][x]', data[y][x])
                # if x_start == -1:
                #     if data[y][x].isnumeric():
                #         number = data[y][x]    
                #         x_start = x
                #     continue
                # if x_start > -1:
                #     if data[y][x].isnumeric():
                #         number += data[y][x]
                #         if x == len(data[y]) - 1:
                #             print(y, x_start, x)
                #             if isSurroundedBySymbol(data, y, x_start, x-1):
                #                 sum += int(number)
                #             x_start = -1
                #             number = ''
                #     else:
                #         print(y, x_start, x)
                #         if isSurroundedBySymbol(data, y, x_start, x-1):
                #             sum += int(number)
                #         x_start = -1
                #         number = ''
        
        if expected == sum:
            print('Sum is: ', sum, 'which is expected')
        else:
            print('Sum is: ', sum, 'which was not expected: [', expected, ']')
            exit(0)
    return 

main(file_name=basic_file_name, expected=expected)
main(file_name=full_file_name)