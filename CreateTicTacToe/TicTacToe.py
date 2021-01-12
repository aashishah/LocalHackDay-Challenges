
import random

board = {7: ' ' , 8: ' ' , 9: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            1: ' ' , 2: ' ' , 3: ' ' }


def printBoard(board):
	k = 0
	for i in [1, 4, 7]:
		print(" " + board[i] + " " + '|' + " " + board[i + 1]  + " " + '|'  + " " + board[i + 2])
		if k < 2:
		 print('---+---+---')
		k += 1

def play():
	count = 0
	player = "X"
	printBoard(board)
	gameOn = True

	while gameOn and count < 10:

		if count % 2 == 0:
			print("It's your move. Move at which place?")
			player = "X"
			humanPlay(board)
		else:
			print("Computer's play:")
			player = "O"
			computerPlay(board)
		count += 1

		if count >= 5:
			gameOn = checkWhoWon(board, player)

	if count == 9:
			print("Tie! Game Over.")

def computerPlay(board):
	comp = 9
	while board[comp] != " ":
		comp = random.randrange(1,10,1)
	
	board[comp] = "O"
	printBoard(board)


def humanPlay(board):
		move = int(input())

		if board[move] == " ":
			board[move] = "X"
			printBoard(board)
		else:
			print("Place has already been filled, enter place again.")
			humanPlay(board)

def checkWhoWon(board, player):
	winPossibilities = [[7,8,9],[4,5,6],[1,2,3],[1,4,7],[2,5,8],[3,6,9],[7,5,3],[1,5,9]]
	for poss in winPossibilities:
		x,y,z = poss
		if board[x] == board[y] == board[z] != " ":
			print("*******Game Over!********")
			if player == "X":
				print("      YOU WON!       ")
			else:
				print("You couldn't beat the computer :(")
			return False

	return True

if __name__ == "__main__":
    play()
