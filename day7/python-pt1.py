import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file))[0]
    _min = 10000000000000000000
    target = 0
    
    optimized = False
    while not optimized:
        _sum = 0
        target = target +1
        for i in range(len(data)):
            distance_to_target = abs(int(data[i]) - target)
            _sum = _sum + distance_to_target   
        if _sum < _min:
            _min = _sum
        else:
            optimized = True
    
    print(_min)
