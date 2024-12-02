import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

max = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def isValid(color_go):
    _, count, color = color_go.split(" ")
    color = color.replace("\n", "")
    if int(count) > max[color]:
        return False
    return True

def isValidTurn(turn):
    colors = turn.split(",")
    for color in colors:
        if not isValid(color):
            return False
    return True

def isValidRow(row):
    turns = row.split(";")
    for turn in turns:
        if not isValidTurn(turn):
            return False
    return True
    
with open(file_name) as file:
    sum = 0
    for row in file:
        id, rest = row.split(":")
        id = int(id.replace("Game ", ""))
        if isValidRow(rest):        
            sum += id

    print('Sum is:', sum)
