import sys

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'


def process_part1(row):
    sum, nums = row.split(":")
    nums = nums.strip().split()

with open(file_name) as file:
    sum_1 = 0
    
    for i, row in enumerate(file):
        sum_1 += process_part1(row)