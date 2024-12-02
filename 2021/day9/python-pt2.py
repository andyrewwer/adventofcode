import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

def check_if_lower_than_neighbors(data, i, j):
    val = int(data[i][j])
    if i == 0 or val < int(data[i-1][j]):
        if i+1 == len(data) or val < int(data[i+1][j]):
            if j == 0 or val < int(data[i][j-1]):
                if j+1 == len(data[i]) or val < int(data[i][j+1]):
                    return True
    return False

def find_low_points(data):
    low_points = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if check_if_lower_than_neighbors(data, i, j):
                low_points.append([i,j])
    return low_points

def find_size_of_basin(data, low_point): 
    # go right until you hit a 9
    # for each cell go down 1
    # then go right until a 9 
    # go down 1 
    # repeat
    # make sure to go left as well just in case. If we save results into set will dedupe duplicate points but catch things like
    # 1 2 2 3 9
    # 1 9 9 3 9
    # 9 9 3 3 9 where if you only go right would miss a three
    # is this even good



with open(file_name) as file:
    data = file.read().splitlines()
    points = find_low_points(data)
    # we know have list of [[x,y], [x,y]] coordinates of low points. Now to find the basin for each one.
    _sum = 0
    for point in points:
        _sum = _sum + int(data[point[0]][point[1]]) + 1
    
    print(points)
    print(_sum)


