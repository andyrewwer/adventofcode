import sys

file_name = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

board_size = 10
winners = [0,0]

def roll_dice(players, turn):
    create_universe(players, turn, 1) 
    create_universe(players, turn, 2) 
    create_universe(players, turn, 3) 

def check_winner(player):
    return player['score'] >= 2
         
def play_turn(player, roll):
    new_pos = (player['pos'] + roll) % board_size
    player['pos'] += new_pos
    player['score'] += board[new_pos]

def create_universe(players, turn, roll):
    print('created universe', turn)
    if check_winner(players[turn]):
        winners[turn] += 1
        print('game-ended', winners)
        return
    next_turn = 1 if turn == 0 else 0
    for i in range(3):
        create_universe(players, next_turn, 1)
        create_universe(players, next_turn, 2)
        create_universe(players, next_turn, 3)

with open(file_name) as file:
    data = file.read().splitlines()
    board = [10]
    for i in range(board_size -1):
        board.append(i+1)
    print(board)

    players = []
    for i in range(len(data)):
        #assumes <10 players always starting 1-9. Super safe assumptions. Probably better way to do this with regex/split on spaces.
        player_num = data[i][7:8]
        player_start = data[i][-1]
        players.append({'player': int(player_num), 'pos': int(player_start), 'score': 0})

    roll_dice(players, 0)

    print('winner', winners)





        


