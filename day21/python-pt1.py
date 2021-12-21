import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

board_size = 10

def roll_dice(next_roll):
    return 3 * (next_roll + 1)

with open(file_name) as file:
    data = file.read().splitlines()
    board = [10]
    for i in range(board_size -1):
        board.append(i+1)
    print(board)

    points = []
    players = []
    for i in range(len(data)):
        #assumes <10 players always starting 1-9. Super safe assumptions. Probably better way to do this with regex/split on spaces.
        player_num = data[i][7:8]
        player_start = data[i][-1]
        players.append({'player': int(player_num), 'pos': int(player_start), 'score': 0})

    winner = -1
    num_rolls = 0;
    next_roll = 1
    while winner < 0:
        for player in players:
            roll = roll_dice(next_roll)
            #only works with board size 10 and dice multiple of 10
            next_roll += 3
            num_rolls += 3
            new_pos = (player['pos'] + roll) % board_size
            player['pos'] = new_pos
            player['score'] += board[new_pos]
            if player['score'] >= 1000:
                winner = player['player']
                break
            print('score', player['score'])
    print('winner', winner)
    loser_score = 0
    if winner == 1:
        loser_score = players[1]['score']
    if winner == 2:
        loser_score = players[0]['score']
    print(loser_score)
    print(num_rolls)
    print(num_rolls * loser_score)




        


