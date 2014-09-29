from random import randint
input = "y"
while input == "y":
	random=randint(1,101)
	for i in range(7):
		print"guess anumber from 1 to 100"
		guess = int(raw_input())

		if guess>random+15:
			print"way to high"
		elif guess>random:
			print "too high"
		elif guess<random-15:
			print" way to low"
		elif guess<random:
			print"to low"
		else:
			print"you won"
			break
	else:
		print"you lost" 
		
	input=raw_input ("do you want to keep playing")