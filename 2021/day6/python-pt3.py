import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]
#could make number a param, for now hardcoding to 80
num_days = 256 

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file))[0]
    print(data)
    current_state = [data.count('0'), data.count('1'), data.count('2'), data.count('3'), data.count('4'), data.count('5'), 0, 0, 0]   
    print(current_state)
    for i in range(num_days):
        print('day', i)
        next_state = [
                current_state[1],
                current_state[2],
                current_state[3],
                current_state[4],
                current_state[5],
                current_state[6],
                current_state[7],
                current_state[8],
                current_state[0]
            ]
        print(current_state)
        if current_state[0] > 0:
            next_state[6] += current_state[0]
        print(next_state)
        current_state = next_state
        next_state = []
    _sum = 0
    for i in range(len(current_state)):
        _sum += current_state[i]
    print(_sum)
