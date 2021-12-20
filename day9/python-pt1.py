import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

with open(file_name) as file:
    data = file.read().splitlines()
    points = []
    _sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            val = int(data[i][j])
            if i == 0 or val < int(data[i-1][j]):
                if i+1 == len(data) or val < int(data[i+1][j]):
                    if j == 0 or val < int(data[i][j-1]):
                        if j+1 == len(data[i]) or val < int(data[i][j+1]):
                            points.append(val)
                            _sum = _sum + 1 + val
    print(points)
    print(_sum)


