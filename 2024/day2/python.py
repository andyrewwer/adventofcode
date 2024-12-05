import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'

def safe_pair(direction, level, next):
    if direction == 1 and level > next:
        return False
    if direction == -1 and level < next:
        return False
    diff = abs(int(level) - int(next))
    if diff < 1 or diff > 3:
        return False
    return True

def process_row_part1(row):
    direction = 0
    for i in range(0, len(row) - 1):
        level = int(row[i])
        next = int(row[i+1])

        if direction == 0:
            direction = -1 if level > next else 1
        
        if not safe_pair(direction, level, next):
            return False
    return True    

def get_list_without_index(row, index):
    if index == 0:
        return row[1:]
    if index == len(row) - 1:
        return row[:-1]
    return row[0:index] + row[index+1:]

def handleFailure(row, i, first):
    if first:
        remove_previous = get_list_without_index(row, i-1)
        remove_current = get_list_without_index(row, i)
        remove_next = get_list_without_index(row, i+1)
        return process_row_part2(remove_previous, first=False) or process_row_part2(remove_current, first=False) or process_row_part2(remove_next, first=False)
    else:
        return False

def process_row_part2(row, first=True):
    direction = 0
    for i in range(0, len(row) - 1):
        level = int(row[i])
        next = int(row[i+1])

        if direction == 0:
            direction = -1 if level > next else 1
            
        if not safe_pair(direction, level, next):
            return handleFailure(row, i, first)

    return True

def part1(csv_reader):
    safe_reports = 0
    for row in csv_reader:
        if process_row_part1(row):
            safe_reports += 1
        
    print('Part 1: The total number of safe reports is ' + str(safe_reports))

def part2(csv_reader):
    safe_reports = 0
    for row in csv_reader:
        if process_row_part2(row):
            safe_reports += 1
        
    print('Part 2: The total number of safe reports is ' + str(safe_reports))


with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    part1(csv_reader)    

with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    part2(csv_reader)    
