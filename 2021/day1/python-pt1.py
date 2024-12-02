import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file)
    count = -1 #offset first row
    prev = 0
    for row in csv_reader:
        cur = int(row[0])
        if cur > prev:
            count = count + 1
        prev = cur

    print(count)
