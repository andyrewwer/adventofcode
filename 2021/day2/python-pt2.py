import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file, delimiter=' '))
    x_pos = 0
    y_pos = 0
    aim = 0
    for i in range(len(data)):
        row = data[i]
        print(row) 
        if row[0] == 'forward':
            x_pos = x_pos + int(row[1])
            y_pos = y_pos + int(row[1]) * aim
        if row[0] == 'down':
            aim = aim + int(row[1])
        if row[0] == 'up':
            aim = aim - int(row[1])

    print('x_pos', x_pos)
    print('y_pos', y_pos)
    print('aim', aim)
    print('total', x_pos * y_pos)
