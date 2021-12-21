import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

def lookup_value(symbol):
    if symbol == '(':
        return 1
    if symbol == '[':
        return 2
    if symbol == '{':
        return 3
    if symbol == '<':
        return 4
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
    return (match_symbol == '(' and next_item == ')') or (match_symbol == '[' and next_item == ']') or (match_symbol == '{' and next_item == '}') or (match_symbol == '<' and next_item == '>')

with open(file_name) as file:
    data = file.read().splitlines()
    _sums = []
    for i in range(len(data)):
        row = data[i]
        _list = []
        isValid = True
        for char in row:
            if is_open(char):
                _list.append(char)
            else:
                item = _list.pop(-1)
                if not matches_close(item, char):
                    isValid = False
                    break
        if isValid:
            _sum = 0
            for i in range(len(_list)):
                _sum = _sum * 5
                _sum += lookup_value(_list.pop(-1))
            _sums.append(_sum)
            print(_sum)

    print(_sums)
    _sums.sort()
    print((len(_sums)+1)/2)
    print(_sums)
    print(_sums[int(len(_sums)/2)])


