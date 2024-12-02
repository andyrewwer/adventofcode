import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

def isValid(color_go, max):
    _, count, color = color_go.split(" ")
    color = color.replace("\n", "")
    print(int(count), max[color])
    if int(count) > max[color]:
        max[color] = int(count)
    return max

def isValidTurn(turn, max):
    colors = turn.split(",")
    for color in colors:
        max = isValid(color, max)
    return max

def isValidRow(row, max):
    turns = row.split(";")
    for turn in turns:
        max = isValidTurn(turn, max)
    return max
    
with open(file_name) as file:
    sum = 0
    for row in file:
        id, rest = row.split(":")
        id = int(id.replace("Game ", ""))
        max = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        max = isValidRow(rest, max)
        sum += max["red"] * max["green"] * max["blue"]

    print('Sum is:', sum)
