import sys

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'

data = []
with open(file_name) as file:
    xmas_count_1 = 0
    xmas_count_2 = 0
    for row in file:
        data.append(row.strip())

    for y in range(0, len(data)):
        for x in range (0, len(data[0])):
            if data[y][x] == "X":
                can_go_up = y-3 >= 0
                can_go_right = x+3 < len(data[y])
                can_go_down = y+3 < len(data)
                can_go_left = x-3 >= 0

                if can_go_up and data[y-1][x] == "M" and data[y-2][x] == "A" and data[y-3][x] == "S":
                    xmas_count_1 +=1

                if can_go_up and can_go_right and data[y-1][x+1] == "M" and data[y-2][x+2] == "A" and data[y-3][x+3] == "S":
                    xmas_count_1 +=1

                if can_go_right and data[y][x+1] == "M" and data[y][x+2] == "A" and data[y][x+3] == "S":
                    xmas_count_1 += 1

                if can_go_down and can_go_right and data[y+1][x+1] == "M" and data[y+2][x+2] == "A" and data[y+3][x+3] == "S":
                    xmas_count_1 += 1

                if can_go_down and data[y+1][x] == "M" and data[y+2][x] == "A" and data[y+3][x] == "S":
                    xmas_count_1 += 1

                if can_go_down and can_go_left and data[y+1][x-1] == "M" and data[y+2][x-2] == "A" and data[y+3][x-3] == "S":
                    xmas_count_1 += 1

                if can_go_left and data[y][x-1] == "M" and data[y][x-2] == "A" and data[y][x-3] == "S":
                    xmas_count_1 += 1

                if can_go_up and can_go_left and data[y-1][x-1] == "M" and data[y-2][x-2] == "A" and data[y-3][x-3] == "S":
                    xmas_count_1 += 1

    for y in range(0, len(data)):
        for x in range (0, len(data[0])):
            if data[y][x] == "A":
                can_go_up = y-1 >= 0
                can_go_right = x+1 < len(data[y])
                can_go_down = y+1 < len(data)
                can_go_left = x-1 >= 0
                if not can_go_up or not can_go_right or not can_go_down or not can_go_left:
                    continue

                if data[y-1][x+1] == data[y-1][x-1] and data[y+1][x+1] == data[y+1][x-1]:
                    if data[y-1][x-1] == "M" and data[y+1][x+1] == "S":
                        xmas_count_2 += 1
                    elif data[y-1][x-1] == "S" and data[y+1][x+1] == "M":
                        xmas_count_2 += 1
                        
                if data[y-1][x-1] == data[y+1][x-1] and data[y+1][x+1] == data[y-1][x+1]:
                    if data[y-1][x-1] == "M" and data[y+1][x+1] == "S":
                        xmas_count_2 += 1
                        
                    elif data[y-1][x-1] == "S" and data[y+1][x+1] == "M":
                        xmas_count_2 += 1
                        
    print('Part 1: The total sum is ' + str(xmas_count_1))
    print('Part 2: The total sum is ' + str(xmas_count_2))