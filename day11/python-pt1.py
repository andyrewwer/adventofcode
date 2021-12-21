import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

def add_one(data, x, y):
    data[x][y] += 1
    if data[x][y] > 9 and data[x][y] < 1000:
        data[x][y] = 1000
        add_to_all_adjacent(data, x, y)

def add_to_all_adjacent(data, x, y): 
    val = data[x][y]
    #orthagonal
    if x > 0:
        add_one(data, x-1, y)
    if x+1 < len(data):
        add_one(data, x+1, y)
    if y > 0:
        add_one(data, x, y-1)
    if y+1 < len(data[y]):
        add_one(data, x, y+1)
    
    #corners
    if x > 0 and y > 0:
        add_one(data, x-1, y-1)
    if x > 0 and y+1 < len(data[y]):
        add_one(data, x-1, y+1)
    if x+1 < len(data[x]) and y > 0:
        add_one(data, x+1, y-1)
    if x+1 < len(data[x]) and y+1 < len(data[y]):
        add_one(data, x+1, y+1)


with open(file_name) as file:
    data = file.read().splitlines()
    flashes = 0
    for i in range(10):
        data[i] = [int(a) for a in data[i]]

    for i in range(100):
        for j in range(len(data)):
            for n in range(len(data[j])):
                add_one(data, j, n)

        for j in range(len(data)):
            for n in range(len(data[j])):
                if data[j][n] >= 1000:
                    data[j][n] = 0 
                    flashes += 1
        print(data)

        print('day ', i+1, ': flashes: ', flashes)
