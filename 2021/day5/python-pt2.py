import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as file:
    data = file.read().splitlines()
    points = []
    for i in range(len(data)):
        row = data[i].split(' -> ')
        first = row[0].split(',')
        second = row[1].split(',')
        max_x = int(max(first[0], second[0]))
        max_y = int(max(first[1], second[1]))
        first_x = int(first[0])
        first_y = int(first[1])
        second_x = int(second[0])
        second_y = int(second[1])
        while max_y >= len(points):
            for j in range(max_y+1):
                if len(points) > j:
                    continue
                points.append([])
        while max_x >= len(points[-1]):
            for j in range(max_x+1):
                for k in range(len(points)):
                    if len(points[k]) > j:
                        continue
                    points[k].append(0)
        if first_x == second_x:
            higher = first_y if first_y > second_y else second_y
            lower = second_y if first_y > second_y else first_y
            while higher >= lower:
                points[lower][first_x] = points[lower][first_x] + 1
                lower = lower + 1
        elif first_y == second_y:
            higher = first_x if first_x > second_x else second_x
            lower = second_x if first_x > second_x else first_x
            while higher >= lower:
                points[first_y][lower] = points[first_y][lower] + 1
                lower = lower + 1
        else:
            higher_x = first_x if first_x > second_x else second_x
            lower_x = second_x if first_x > second_x else first_x
            higher_y = first_y if first_x > second_x else second_y
            lower_y = second_y if first_x > second_x else first_y
            while higher_x >= lower_x:
                points[lower_y][lower_x] = points[lower_y][lower_x] + 1
                lower_y = lower_y + 1 if lower_y < higher_y else lower_y - 1
                lower_x = lower_x +1 
                # pretty sure could refactor all to use this logic and only change what gets incremented... Not sure that's easier
    count = 0
    for j in range(len(points)):
        for k in range(len(points[j])):
            if points[j][k] > 1:
                count = count + 1
    print(count)
