import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

def getFirstDigit(string):
    for c in string:
        if c.isnumeric():
            return c
        
def getLastDigit(string):
    for c in string[::-1]:
        if c.isnumeric():
            return c


with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file)
    sum = 0
    for row in csv_reader:
        number = getFirstDigit(row[0]) + getLastDigit(row[0])
        sum += int(number)
        print(number)
        
    print('Sum is:', sum)
