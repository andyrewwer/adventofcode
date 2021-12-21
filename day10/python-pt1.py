import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

def lookup_value(symbol):
    if symbol == ')':
        return 3
    if symbol == ']':
        return 57
    if symbol == '}':
        return 1197
    if symbol == '>':
        return 25137

def is_open(symbol):
    return symbol in ['(', '[', '{', '<']

def matches_close(match_symbol, next_item):
zsh:1: command not found: qq

with open(file_name) as file:
    data = file.read().splitlines()
    _sum = 0
    for row in data:
        _list = []
        for char in row:
            if is_open(char):
                _list.append(char)
            else:
                item = _list.pop(-1)
                if not matches_close(item, char):
                    _sum += lookup_value(char)               
    print(_sum)



