import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]
#could make number a param, for now hardcoding to 80
num_days = 256
init_data = [[], [1], [2], [3], [4], [5]]

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file))[0]
    for i in range(num_days):
        print('day', i)
        for j in range(len(init_data)):
            print('processing:', j)
            for k in range(len(init_data[j])):
                init_data[j][k] = int(init_data[j][k])-1
                if init_data[j][k] == -1:
                    init_data[j][k] = 6
                    init_data[j].append(8)
    counts = [0, 0, 0, 0, 0, 0]
    for i in range(len(data)):
        print(data[i])
        counts[int(data[i])] = counts[int(data[i])] + 1
    print(counts)
    _sum = 0
    for i in range(len(counts)):
        _sum = _sum + counts[i] * len(init_data[i])   
    print(_sum)
