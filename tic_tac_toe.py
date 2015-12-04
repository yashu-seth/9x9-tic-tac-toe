def gameplay(board, player):
	if board.complete():
		winner = board.winner()
		if winner =='X': return 1
		if winner=='O': return -1
		return 0;
	best_move = None
	for move in board.possible_moves():
		board.make_move(move, player)
		this_move = gameplay(board, get_enemy(player))
		board.make_move(move, None)
		if player=='X':
			if this_move>best_move:
				best_move = this_move
		if player=='O':
			if this_move<best_move:
				best_move = this_move
	return best_move

def get_enemy(player):
	if player=='X': return 'O'
	return 'X'

class Tic(object):

	winning_combos = [[0,1,2], [3,4,5], [6,7,8],[0,3,6], [1,4,7], [2,5,8], [0,5,8], [2,5,7]]

	def __init__(self, squares=[]):
		self.squares = [None,None,None,None,None,
						None,None,None,None]

	def get_squares(self):
		return self.squares

	def make_move(self, move, player):
		self.squares[move] = player

	def possible_moves(self):
		pos_moves = []
		for i in range(9):
			if self.squares[i]==None: pos_moves.append(i)
		return pos_moves

	def winner(self):
		x = 0
		o = 0
		for combo in self.winning_combos:
			for sq in combo:
				if self.squares[sq] == 'X': x+=1
				if self.squares[sq] == 'O': o+=1
			if x==3: return 'X'
			x = 0
			if o==3: return 'O'
			o = 0
		return None

	def complete(self):
		if None not in self.squares: return 1
		if self.winner == 'X' or self.winner == 'O': return 1
		return 0
    
def start_play(play):
    print("entry1")
    while(play.complete()==0):
        print("make your move")
        human_move = int(input())
        play.make_move(human_move, 'O')
        print(play.get_squares())
        score = -2
        for move in play.possible_moves():
                move_score = gameplay(play, 'X')
                if move_score>score:
                        cpu_move = move
        play.make_move(cpu_move, 'X')
        print(play.get_squares())
    print(play.winner())

play = Tic()
start_play(play)

