from random import randint

def printBoard():
	print board[0] + " | " + board[1] + " | " + board[2]
	print "---------"
	print board[3] + " | " + board[4] + " | " + board[5]
	print "---------"
	print board[6] + " | " + board[7] + " | " + board[8]

def checkWin(cur):
	# cur is the last move, that way only check moves related
	return False

def checkLoss(cur):
	return False

board = []

for i in range(9):
	board.append(str(i))

playing = True

while playing:
	printBoard()
	input = int(raw_input("Choose an option (-1 to quit): "))
	if input == -1:
		playing = False
		break
	if input < 0 or input > 8:
		print "Not a valid option"
		continue
	if board[input] == "X" or board[input] == "O":
		print "That spot has been taken"
		continue
	board[input] = "X"

	if checkWin(input):
		playing = False
		print "You win!"
		break

	valid = []
	for i in range(9):
		if board[i] != "X" and board[i] != "O":
			valid.append(i)

	num = valid[randint(0, len(valid)-1)]
	board[num] = "O"

	if checkLoss(num):
		playing = False
		print "You lose"
		break

print "Thanks for playing!"