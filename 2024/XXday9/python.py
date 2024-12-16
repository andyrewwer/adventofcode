# import sys, time

# file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'
# input_data = []
# with open(file_name, "r") as file:
#   content = file.readlines()
#   for line in content:
#       input_data.append(line.strip())

# input_data[0] = [int(val) for val in input_data[0]]


# processed_line = []
# count = 0
# for line in input_data:
#     is_zero = True
#     for num in line:
#         num = int(num)
#         if is_zero:
#             processed_line.extend([count] * num)
#             count += 1
#         else:
#             processed_line.extend([None] * num)
#         is_zero = not is_zero

# # print(processed_line)

# def part_one(strip):
    
#     free_space = strip.index(None)
#     for i in reversed(range(0, len(strip))):
#         if strip[i] is not None:
#             strip[free_space] = strip[i]
#             strip[i] = None
#             while strip[free_space] is not None:
#                 free_space += 1
#             if i - free_space <= 1:
#                 break

#     answer = sum(val * itx if val is not None else 0 for (itx, val) in enumerate(strip))
#     print(f"Part 1: {answer}")


#     return answer, strip


# def part_1(line):
#     answer = 0
#     answer_2 = 0
#     i = 0
#     j = len(line) - 1
#     while i <= j:
#         el = line[i]
#         while el == None:
#             if i > j:
#                 el = 0
#                 break
#             line[i] = line[j]
#             el = line[j]
#             line[j] = None
#             j -= 1

#         answer_2 += i * el
#         # print(i, int(el), i * int(el), sum,)
#         i +=1
#     answer = sum(val * itx if val is not None else 0 for (itx, val) in enumerate(line))
#     # print(answer_2)
#     return answer, line



# answer, output_line_1 = part_one(processed_line) 
# # print(output_line_1)
# print(sum(val * itx if val is not None else 0 for (itx, val) in enumerate(output_line_1)))


# answer, output_line_2 = part_1(processed_line)
# # print(output_line_2)
# # print(answer)
# print(sum(val * itx if val is not None else 0 for (itx, val) in enumerate(output_line_2)))


# print(output_line_1 == output_line_2)

# # 6384282084737


#!/bin/python3

import sys
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.csv"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # lines.append(list(line))
            lines.append(line)

    return lines


def part_one():
    lines = read_lines_to_list()
    vals = [int(val) for val in list(lines[0])]
    answer = 0

    id = 0
    strip = []
    is_block = True
    for i in range(len(vals)):
        if is_block:
            strip.extend([id] * vals[i])
            id += 1
        else:
            strip.extend([None] * vals[i])

        is_block = not is_block

    free_space = strip.index(None)
    for i in reversed(range(0, len(strip))):
        if strip[i] is not None:
            strip[free_space] = strip[i]
            strip[i] = None
            while strip[free_space] is not None:
                free_space += 1
            if i - free_space <= 1:
                break

    answer = sum(val * itx if val is not None else 0 for (itx, val) in enumerate(strip))
    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    vals = [int(val) for val in list(lines[0])]
    answer = 0

    id = 0
    strip = []
    gaps = []
    blocks = []
    is_block = True
    for i in range(len(vals)):
        if is_block:
            blocks.append((len(strip), id, vals[i]))
            strip.extend([id] * vals[i])
            id += 1
        else:
            gaps.append((vals[i], len(strip)))
            strip.extend([None] * vals[i])

        is_block = not is_block

    for block in reversed(blocks):
        (position, id, length) = block
        for itx, (gap_length, gap_position) in enumerate(gaps):
            if gap_position > position:
                break

            if gap_length >= length:
                for l in range(length):
                    strip[position + l] = None
                    strip[gap_position + l] = id

                diff = gap_length - length
                if diff > 0:
                    gaps[itx] = (diff, gap_position + length)
                else:
                    gaps.pop(itx)
                break

    answer = sum(val * itx if val is not None else 0 for (itx, val) in enumerate(strip))

    print(f"Part 2: {answer}")


part_one()
part_two()