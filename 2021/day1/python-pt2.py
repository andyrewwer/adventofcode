import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file))
    count = -1 #offset first row
    prev = 0
    for i in range(len(data)):
        if len(data) == i + 2:
            break
        # could for loop through an input to be more generic. Hard coded to 3-length array.
        cur = int(data[i][0]) + int(data[i+1][0]) + int(data[i+2][0])

        #could avoid saving prev by doing computation again. Depends if compute or storage cheaper
        if cur > prev:
            count = count + 1
        prev = cur

    print(count)
