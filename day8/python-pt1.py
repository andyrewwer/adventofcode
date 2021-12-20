import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as file:
    data = file.read().splitlines()
    count = 0
    for row in data:
        digits = row.split('|')[1].split()
        for digit in digits:
            if len(digit) in [2,3,4,7]:
                count = count + 1



#1 = 2
#4 = 4
#7 = 3
#8 = 7

    print(count)
