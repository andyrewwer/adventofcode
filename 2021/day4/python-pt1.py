import csv
import sys

file_name = 'input.csv' if len(sys.argv) < 2 else sys.argv[1]

def get_bingo_numbers(data, num_rows):
    result = []
    for i in range(num_rows):
        row = data[i][0]
        for val in row.split(','):
            result.append(val)
    return result

def get_bingo_cards(data):
    result = []
    next_card = []
    for i in range(len(data)):
        row = data[i]
        if len(row) == 0:
            continue
        row_data = []
        for j in range(len(row)):
            if len(row[j]) == 0:
                continue
            row_data.append(row[j])
        next_card.append(row_data)
        if len(next_card) == 5:
            result.append(next_card)
            next_card = []
    return result

def check_if_winner(card):
    winner = False
    unmarked_total = 0
    column_result = []
    for i in range(len(card)):
        row = card[i]
        row_count = 0
        for j in range(len(row)):
            if len(column_result) == j:
                column_result.append(0)
            value = row[j]
            if value == 'X':
                row_count = row_count + 1
                column_result[j] = column_result[j] + 1
                if row_count == len(row) or column_result[j] == len(row):
                    winner = True
                    print(card)
            else:
                unmarked_total = unmarked_total + int(value)
    return unmarked_total if winner else -1

def mark_bingo_card(cards, value):
    for i in range(len(cards)):
        card = cards[i]
        for j in range(len(card)):
            row = card[j]
            for k in range(len(row)):
                val = row[k]
                if val == value:
                    cards[i][j][k] = 'X'
                    total = check_if_winner(card)
                    if total > -1:
                        return total
    return -1

with open(file_name) as csv_file:
    data = list(csv.reader(csv_file, delimiter=' '))
    bingo_nums = get_bingo_numbers(data, 1)
    data.pop(0) #remove header row
    bingo_cards = get_bingo_cards(data)
    winner = False
    total = -1
    while total == -1 and len(bingo_nums) > 0:
        next_num = bingo_nums.pop(0)
        total = mark_bingo_card(bingo_cards, next_num)
    print(next_num)
    print(total)
    print(int(next_num) * int(total))
