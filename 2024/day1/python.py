import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

def part1(left_list, right_list):
    left_list.sort()
    right_list.sort()

    diff = 0
    for i in range (0, len(left_list)):
        diff = diff + abs(int(left_list[i]) - int(right_list[i]))
    
    print('Part 1: The total difference is ' + str(diff))

def part2(left_list, right_map):
    similarity = 0
    for item in left_list:
        if item not in right_map:
            continue
        similarity = similarity + (int(item) * right_map[item])
    print('Part 2: The total similarity is ' + str(similarity))


with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file)
    left_list = []
    right_list = []
    right_map = {}
    for row in csv_reader:
        left, right = row[0].split("  ")
        right = right.strip()
        left_list.append(left)
        #part 1 
        right_list.append(right)
        #part 2
        if right not in right_map:
            right_map[right] = 0
        right_map[right] = right_map[right] + 1
        
    part1(left_list, right_list)
    part2(left_list, right_map)