import sys, time

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'
grid = {}
zero_pos = []
with open(file_name, "r") as file:
  content = file.readlines()
  for y, line in enumerate(content):
      line = line.strip()
      for x, el in enumerate(line):
            el = int(el)
            grid[(y,x)] = el
            if el == 0:
                zero_pos.append((y,x))

directions = [(1,0), (0,1), (-1,0), (0,-1)]

trails = {}

def recurse(pos, search, max, start):
    if grid[pos] == max:
        if start not in trails:
            trails[start] = list()
        trails[start].append(pos)
        return
    for dir in directions:
        new_pos_y, new_pos_x = pos[0] + dir[0], pos[1] + dir[1]
        new_pos = (new_pos_y, new_pos_x)
        if new_pos in grid and grid[new_pos] == search:
            recurse(new_pos, search + 1, max, start)

for pos in zero_pos:
    recurse(pos, 1, 9, pos)

sum_part_1 = 0
sum_part_2 = 0
for pos in trails:
    # print(len(trails[pos]))
    trail_set = set(trails[pos])
    sum_part_1 += len(trail_set)
    sum_part_2 += len(trails[pos])

print(sum_part_1)
print(sum_part_2)
