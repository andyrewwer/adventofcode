import sys, time

file_name = 'input.csv' if len(sys.argv) < 2 else 'input-basic.csv'
input_data = []
with open(file_name, "r") as file:
  content = file.readlines()
  for line in content:
      input_data.append(line.strip())

antennas = {}

for y, line in enumerate(input_data):
    for x, el in enumerate(line):
        if el != ".":
            if el not in antennas:
                antennas[el] = []
            antennas[el].append((y,x))

pairs = set()

def in_bounds(loc, x, y):
    return 0 <= loc[0] < x + 1 and 0 <= loc[1] < y + 1

for key in antennas.keys():
    for i, v1 in enumerate(antennas[key]):
        for j in range(i + 1, len(antennas[key])):
            v2 = antennas[key][j]

            y_dif, x_dif = v1[0] - v2[0], v1[1] - v2[1]

            k = 0
            while in_bounds((v1[0] + y_dif * k, v1[1] + x_dif * k), x, y):
                pairs.add((v1[0] + y_dif * k, v1[1] + x_dif * k))
                k += 1
                
            k = 0
            while in_bounds((v2[0] + y_dif * k, v2[1] + x_dif * k), x, y):
                pairs.add((v2[0] + y_dif * k, v2[1] + x_dif * k))
                k -= 1            

valid_pairs = []
for pair in pairs:
    if 0 <= pair[0] < x + 1 and 0 <= pair[1] < y + 1:
        valid_pairs.append(pair)

print(f"valid_pairs = {len(valid_pairs)}")