import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file))
    count = -1 #offset first row
    prev = 0
    zeros = []
    ones = []
    for i in range(len(data)):
        row = data[i][0]
        for j in range(len(row)):
            if len(zeros) == j :
                print('initializing')
                zeros.append(0)
                ones.append(0)
            if row[j] == '0':
                zeros[j] = zeros[j] + 1
            else:
                ones[j] = ones[j] + 1
    print(zeros)
    print(ones)

    gamma = ''
    epsilon = ''

    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else: 
            gamma = gamma + '1'
            epsilon = epsilon + '0'
    
    print(gamma, int(gamma, 2))
    print(epsilon, int(epsilon, 2))
    print('total', int(gamma,2) * int(epsilon,2))
