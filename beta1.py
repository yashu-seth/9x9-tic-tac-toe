import random

class Tic(object):

    winning_combos = [[0,1,2], [3,4,5], [6,7,8],[0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self, squares=[]):
        if not squares:
            self.squares = [None,]*9
        else: 
            self.squares = squares

    def display_board(self):
        print(self.squares[0:3])
        print(self.squares[3:6])
        print(self.squares[6:9])
        
    def get_squares(self):
        return self.squares

    def make_move(self, move, player):
        self.squares[move] = player

    def possible_moves(self):
        return list(index for index,sq in enumerate(self.squares) if not sq)

    def winner(self):
        x = 0
        o = 0
        for combo in self.winning_combos:
            for sq in combo:
                if self.squares[sq] == 'X': x+=1
                if self.squares[sq] == 'O': o+=1
            if x==3:
                return 'X'
            x = 0
            if o==3: return 'O'
            o = 0
        return None

    def complete(self):
        return any([None not in self.squares, self.winner() == 'X', self.winner() == 'O'])

def get_enemy(player):
    if player=='X': 
        return 'O'
    return 'X'


def gameplay(board, player, alpha, beta):
    if board.complete():
        winner = board.winner()
        if winner =='X':
            return 1
        if winner=='O':
            return -1
        return 0
    moves_score = []
    for move in board.possible_moves():
        board.make_move(move, player)
        this_move_score = gameplay(board, get_enemy(player), alpha, beta)
        board.make_move(move, None)
        y = this_move_score
        if player=='X':
            if y>alpha: alpha = y
            if alpha>=beta:
                return beta
        if player=='O':
            if y<beta: beta = y
            if beta<=alpha:
                return alpha
    if player=='X':
        return alpha
    else:
        return beta
            
##        moves_score.append(this_move_score)
##    if player == 'X': return max(moves_score)
##    else: return min(moves_score)

def get_enemy(player):
    if player=='X': return 'O'
    return 'X'

    
def start_play(play):
##    print("entry1")
    while(play.complete()==0):
        print('\n')
##        print(play.display_board())
        print("make your move")
        human_move = int(input())-1
        if human_move not in play.possible_moves():
            print("invalid move")
            continue
            print('\n')
##        human_move-=1
        play.make_move(human_move, 'O')
        print('\n')
        play.display_board()
        if(play.winner()=='O'): break 
        score = -2
        cpu_best_moves = []
        if len(play.possible_moves())==0: break
        for move in play.possible_moves():
##            print('move no', move)
            play.make_move(move,'X')
            move_score = gameplay(play, 'O', -2, 2)
            play.make_move(move, None)
##            print('move_score', move_score)
            if move_score>score:
                score = move_score
                cpu_best_moves = [move]
            elif move_score==score:
                cpu_best_moves.append(move)
##        cpu_move = random.choice(cpu_best_moves)
##        print(cpu_best_moves)
        cpu_move = (cpu_best_moves)[0]
        play.make_move(cpu_move, 'X')
        print('\n')
        play.display_board()
    print('\n')
    print('The winner is', play.winner())

play = Tic()
start_play(play)
