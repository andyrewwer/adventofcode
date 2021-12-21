import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]
#could make number a param, for now hardcoding to 80
num_days = 256

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file))[0]
    for i in range(num_days):
        print('day ', i)
        for j in range(len(data)):
            data[j] = int(data[j])-1
            if data[j] == -1:
                data[j] = 6
                data.append(8)
    print(len(data))
