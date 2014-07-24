'''
def functionname(parameters):
	"Documentation string"
	code
	return [something]
'''

def get_input():
	"grab 2 numbers and return input"
	input1 = int(raw_input("Enter the first number:"))
	input2 = int(raw_input("enter the second number"))
	return input1, input2

# Addition function
def addition():
	"adds 2 numbers"
	input = get_input()
	return input[0]+input[1]

# Subtraction function
def subtraction(input1,input2):
	"subtracts two numbers"
	return input1-input2

# Multiplication function
def multiplication():
	"mutiplies 2 numbers"
	input = get_input()
	return input[0]*input[1]

# Division function
def division():
	"divides 2 numbers"
	input = get_input()
	if input[1]==0:
		return "you can't divide by 0"
	return input[0]/input[1]


input = 0
while input != -1:
	print "Welcome to the calculator!"
	print "What would you like to do?"
	print "1. Addition"
	print "2. Subtraction"
	print "3. Multiplication"
	print "4. Division"
	input = int(raw_input("Enter your selection (-1 to quit): "))

	if input == 1:
		print addition()
	elif input == 2:
		number_input = get_input()
		value = subtraction(number_input[0],number_input[1])
		print value
	elif input == 3:
		print multiplication()
	elif input == 4:
		print division()
	elif input == -1:
		print "Thanks for using the calculator!"
	else:
		print "Not valid input"