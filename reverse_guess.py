def midpoint(low,high):
	return (low+ high)/2

print "Think of a number between 1 and 100"
low = 1
high = 100
while True:
	guess = midpoint(low, high)
	print "I guess", guess
	print "1. Way too low"
	print "2. Too low"
	print "3. Too high"
	print "4. Way too high"
	print "5. Correct!"
	input = int(raw_input("pick one"))
	if input == 1:
		# it's way  to low
		low = guess+15
	elif input == 2:
		# too low
		low = guess
	elif input == 3:
		# too high
		high = guess
	elif input == 4:
		# way too high
		high = guess-15
	elif input == 5:
		# Correct
		print "I won"
		break
	else:
		print "Invalid input"
