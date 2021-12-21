import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as file:
    data = file.read().splitlines()
    points = []
    for i in range(893):
    #for i in range(15):
        points.append([])
        for j in range(1311):
        #for j in range(11):
            points[i].append('.')
    
    instruction_count = 0
    for i in range(len(data)):
        if len(data[i]) == 0:
            #blank line separating data from folds
            print('blank line')
            continue
        elif data[i][0].isnumeric():
            print('building data')
            xy = data[i].split(',')
            points[int(xy[1])][int(xy[0])] = '#'
        else:
            instruction_count += 1
            instructions = data[i][11:].split('=')
            fold = int(instructions[1])
            print('fold instruction', instructions)
            if instructions[0] == 'y':
                length = 1
                while True:
                    if fold + 1 == len(points) or fold - length < 0:
                        break
                    upper_row = points[fold-length]
                    lower_row = points[fold+1]
                    for j in range(len(upper_row)):
                        if lower_row[j] == '#':
                            points[fold-length][j] = '#'
                    points.pop(fold+1)
                    length += 1
            if instructions[0] == 'x':
                for j in range(len(points)):
                    length = 1
                    fold_complete = False
                    while not fold_complete:
                        if fold + 1 == len(points[j]) or fold - length < 0:
                            fold_complete = True
                            break
                        right = points[j][fold+1]
                        left = points[j][fold-length]
                        if right == '#':
                            points[j][fold-length] = '#'
                        points[j].pop(fold+1)
                        length += 1
          #  if instruction_count == 1:
               # break

    _sum = 0
    for row in points:
        print(row)
        for point in row:
            if point == 1:
                _sum += 1
    print(_sum)




        


