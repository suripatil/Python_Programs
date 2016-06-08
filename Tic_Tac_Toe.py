#!/usr/bin/python

import random

# TIC- TAC TOE GAME Simulation (2 Player , Random Positions)
# X | O | X
# ----------
# X | O | X
# ----------
# O | X | X

def fill_tic_tac():
	#remove from the position list since this position is occupied
	#randomly select player and position mark on the matrix
	position = [0,1,2,3,4,5,6,7,8]
	box = [0]*(9)
	flag = True
	#Marking the Box
	for i in range(9):
		#Select Random Position in Matrix
		pos = random.choice(position)
		#Delete the position from original position
		position.remove(pos)
		#Select the Random player and Insert Player 1 -> 'X' ,Player 2 -> 'O'
		pl = random.randint(1,2)
		if(pl == 1):
			box[pos] = 'X'
			#Check_Winner here
			if(check_winner(box,'X')):
				flag = False
				print("*** Player 1 - X Is Winner *** ")
				break
		else:
			box[pos] = 'Y'
			#Check Winner Here
			if(check_winner(box,'Y')):
				flag = False
				print("*** Player 2 - Y Is Winner *** ")
				break
	print_tic_tac(box)
	if(flag):
		print("Game Was Draw !!")

def print_tic_tac(box):
	for i in range(9):
		print(box[i]),
		if ((i+1) % 3 == 0):
			print("")
			print("---------")
		
def check_winner(box,le):
	return ((box[0] == le and box[1] == le and box[2] == le) or 
	(box[3] == le and box[4] == le and box[5] == le) or 
	(box[6] == le and box[7] == le and box[8] == le) or #
	(box[0] == le and box[3] == le and box[6] == le) or 
	(box[1] == le and box[4] == le and box[7] == le) or 
	(box[2] == le and box[5] == le and box[8] == le) or 
	(box[0] == le and box[4] == le and box[8] == le) or 
	(box[2] == le and box[5] == le and box[8] == le)) #Diagonal
	
if __name__ == '__main__':
	
	fill_tic_tac()

