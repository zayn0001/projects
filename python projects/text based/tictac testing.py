#import time
#start = time.perf_counter()
from collections import UserDict

player1 = {'name':'', 'marker':'', 'positions': '', 'turn':True}
player2 = {'name':'', 'marker':'', 'positions': '', 'turn':False}
game_board = {'7' : ' ', '8' : ' ', '9' : ' ',
              '4' : ' ', '5' : ' ', '6' : ' ',
                  '1' : ' ', '2' : ' ', '3' : ' '}
class board():

	
	def __init__(self):
		setattr(self, pos, '')

	def __setitem__(self, pos, marker):
		self.pos

		

	def print(self):
		print('      |     |      ')
		print('   {}  |  {}  |  {}   '.format(self.pos7, self.pos8, self.pos9))
		print('      |     |      ')
		print('===================')
		print('      |     |      ')
		print('   {}  |  {}  |  {}   '.format(self.pos4, self.pos5, self.pos6))
		print('      |     |      ')
		print('===================')
		print('      |     |      ')
		print('   {}  |  {}  |  {}   '.format(self.pos1, self.pos2, self.pos3))
		print('      |     |      ')

	def clear_screen(self):
		print('\n'*100)

	def place_marker(position, marker):
        self.key = marker

	def input_details():
    	global player1
    	global player2
    	player1['name'] = input('Player 1: Enter your name\n')
    	clear_screen()
    	player2['name'] = input('Player 2: Enter your name\n')
    	clear_screen()

	def assign_markers():
    	global player2
    	global player1
    	player1['marker'] = input(player1['name'] + ', Would you like to be X or O\n').upper()
    	if player1['marker'] == 'X':
        	player2['marker'] = 'O'
        	player1['turn'] = True
        	player2['turn'] = False

    	elif player1['marker'] == 'O':
        	player2['marker'] = 'X'
        	player1['turn'] = False
        	player2['turn'] = True
    	else:
        	print("Please choose either X or O")
        	assign_markers()
    	clear_screen()

def recieve_input_pos():
    while True:
        try:
            input_pos = input()
            game_board[input_pos]
        except:
            continue
        else:
            if game_board[input_pos] == ' ':
                break
    return input_pos

winner = 'Tie'
def gameover(player):
    global winner
    if ' ' not in game_board.values():
        return True

    wins = ['123', '456', '789', '147', '258', '369', '357', '159']
    for i in wins:
        if game_board[i[0]] == game_board[i[1]] == game_board[i[2]] == player['marker']:
            winner = player['name']
            return True
    return False
    
def end():
    print('Game Over')
    if winner != 'Tie':
        print(f'{winner} Won!')
    else:
        print('Tie Game')

if __name__ == '__main__':
    clear_screen()
    #print(time.perf_counter() - start)
    input_details()
    assign_markers()
    print_board()
    in_game = True
    while in_game:
        if player1['turn']:
            print(f"{player1['name']}'s Turn")
            input_position = recieve_input_pos()
            place_marker(input_position, player1['marker'])
            clear_screen()
            print_board()
            in_game = not(gameover(player1))
            player1['turn'] = False
            player2['turn'] = True

        elif player2['turn']:
            print(f"{player2['name']}'s Turn")
            input_position = recieve_input_pos()
            place_marker(input_position, player2['marker'])
            clear_screen()
            print_board()
            in_game = not gameover(player2)
            player2['turn'] = False
            player1['turn'] = True
    end()
