import random

class SmallBoard(object):

    winning_combos = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],
                      [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self, squares=[]):
        if len(squares)==0:
            self.squares = [None,]*9
        else: self.squares = squares

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

    def empty(self):
        c = 1
        for x in self.get_squares():
            if x: c = 0
        return c

    def only_one_O(self):
        c = 0
        for x in self.get_squares():
            if x=='O': c+=1
        if c==1: return 1
        else: return 0




class BigBoard(object):

    winning_combos = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],
                      [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self, board_squares = []):
        self.big_board = []
        if len(board_squares)==0:
            for i in range(9):
                k = SmallBoard()
                self.big_board.append(k)
        else:
            for x in board_squares:
                self.big_board.append(x)

    def display_board(self, last_move=[None,None]):
        b = self.get_big_squares()
        t1 = []
        for k in range(9):
            t1.append(b[k].get_squares())
        i,j = 0,0


        
        print('-------------------------------------------------------------')
        for k in range(9):
            x = [t1[i][j], t1[i][j+1], t1[i][j+2],
                  t1[i+1][j], t1[i+1][j+1], t1[i+1][j+2],
                  t1[i+2][j], t1[i+2][j+1], t1[i+2][j+2]]
            
            for z in range(len(x)):
                if x[z]!=None:
                    x[z]= ' '+x[z]+'  '
                    
            print(x[0],x[1],x[2],'      ',
                  x[3],x[4],x[5],'      ',
                  x[6],x[7],x[8])
            
            j+=3
            if (k+1)%3 == 0:
                print()
                j = 0
                i+=3

    def get_big_squares(self):
        return self.big_board
    
    def make_move(self, small_board, small_move, player):
        small_board.make_move(small_move, player)

    def possible_big_moves(self, prev_small_move):
        pos_moves = []
        if self.big_board[prev_small_move].complete():
            for x in self.big_board:
                if x.complete(): continue
                pos_moves.append(x)
        else:
            pos_moves = [self.big_board[prev_small_move]]
        return pos_moves

    def winner(self):
        for x in self.big_board:
            if x.winner(): return x.winner()
        return None

    def complete(self):
        if self.winner(): return 1
        return 0


def get_enemy(player):
    if player=='X': return 'O'
    return 'X'        


def minimax(big_board, prev_small_move, player, alpha, beta, inception):
    if inception>=7:
        return 0
    small_board = big_board.get_big_squares()[prev_small_move]
    if big_board.complete():
        winner = big_board.winner()
        if winner =='X':
            return 1
        if winner=='O':
            return -1
        return 0
    pos_big_moves = big_board.possible_big_moves(prev_small_move)
    moves_score = []
    for x in pos_big_moves:
        for move in x.possible_moves():
            big_board.make_move(x, move, player)
            this_move_score = minimax(big_board, move, get_enemy(player), alpha, beta, inception+1)
            big_board.make_move(x, move, None)
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
            
####            moves_score.append(this_move_score)
####    if player == 'X': return max(moves_score)
####    else: return min(moves_score)

def best_move(big_board, prev_small_move, player):
    cpu_best_moves = []
    score = -2
    pos_big_moves = big_board.possible_big_moves(prev_small_move)
    for x in pos_big_moves:
        for move in x.possible_moves():
            big_board.make_move(x, move, player)
            move_score = minimax(big_board, move, get_enemy(player), -2, 2, 1)
            big_board.make_move(x, move, None)
            if move_score>score:
                score = move_score
                cpu_best_moves = [move]
            elif move_score==score:
                cpu_best_moves.append(move)
    cpu_move = random.choice(cpu_best_moves)
    return cpu_move
            
            


def play_game(game):
    prev_small_move = [0,1,2,3,4,5,6,7,8]
    while(game.complete()==0):
        print()
        print("MAKE YOUR MOVE")
        big_move, small_move = (int(x) for x in input().split())
        big_move-=1
        small_move-=1
        s_move_board = game.get_big_squares()[big_move]
        s_move_list = s_move_board.get_squares()
        invalid_move_flag = 0
        if big_move not in prev_small_move: invalid_move_flag = 1
        if s_move_list[small_move]!=None: invalid_move_flag = 1
        if invalid_move_flag:
            print()
            print("Invalid Move")
            print()
            continue
        game.make_move(s_move_board, small_move, 'O')
        game.display_board()
        if game.winner()=='O': break
        cpu_move = best_move(game, small_move, 'X')
        cpu_move_board = game.get_big_squares()[small_move]
        game.make_move(cpu_move_board, cpu_move, 'X')
        game.display_board()
        prev_small_move = [cpu_move]
    print()
    print("The winner is", game.winner())
    
game = BigBoard()
game.display_board()
play_game(game)


    
