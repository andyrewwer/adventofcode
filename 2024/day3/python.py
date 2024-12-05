import sys
import re

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'

def parse(match):
    # print(match)
    subset = re.search("mul\(\d{1,3},\d{1,3}\)", match).group()
    match = match[match.index(subset):]
    list = match.replace("mul(", "").replace(")", "").split(",")
    # print (list)
    return list

def part1(row):
    sum = 0
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", row)
    for match in matches:
        left,right = parse(match)
        sum += int(left) * int(right)
    
    return sum

def part2(row):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, row)
    
    sum = 0
    flag = True
    for match in matches:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                x,y = map(int, match[4:-1].split(","))
                sum += x*y
    return sum


with open(file_name) as file:
    sum1 = 0
    sum2 = 0
    for row in file:
        # sum1 += part1(row)
        sum2 += part2(row)
    
    print('Part 1: The total sum is ' + str(sum1))
    print('Part 2: The total sum is ' + str(sum2))
