from random import randint
words = ["python", "coding", "computer", "ice", "cream", "sam", "cheese"]
hangman = ["", " O", " O\n |\n |", " O\n\|\n |", " O\n\|/\n |", " O\n\|/\n |\n/"]
lower = 0
upper = len(words)-1
num = randint(lower,upper)
random = words[num]
underscore = ""
length = len(random)
for i in range(length):
	underscore += "_"
wrong = 0
while wrong< 6:
	print hangman[wrong]
	print "the current word is", underscore
	input = raw_input("guess a letter")
	if len(input) != 1:
		print"don't put more than one letter"
		continue
	index = random.find(input)
	if index == -1:
		print"failure"
		wrong += 1 # wrong = wrong + 1
	else:
		underscore = underscore[:index] + input + underscore[index+1:]
		if underscore == random:
			print "you won"
			break
else:
	print "you lost"
	print" O\n\\|/\n |\n/ \\"
