from random import randint

def printBoard():
	print " " + board[0] + " | " + board[1] + " | " + board[2]
	print "-----------"
	print " " + board[3] + " | " + board[4] + " | " + board[5]
	print "-----------"
	print " " + board[6] + " | " + board[7] + " | " + board[8]

board =[]
for i in range (9):
	board.append(str(i))

print "wecome to tictactoe"
while True:
	printBoard()
	print "pick one number on the board "
	input = int(raw_input())
	if input > 8 or input < 0:
		print "you can't pick a number lower than 0 or higher then 8"
		continue
	if board[input] == "x" or board[input] == "o":
		print "that spot is taken"
		continue
	board[input] = "x"

	while True:
		random_guess = randint(0,8)
		if board[random_guess] == "x" or board[random_guess] == "o":
		



