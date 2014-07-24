
def functionname(parameters):
	"Documentation string"
	code
	return [something]

value = functionname(parameters)

def printme(str):
	"Prints out a statement"
	print str
	return

def printthree(str):
	"Prints out a statement three times"
	print str * 3
	return

def print_hangman():
	print " O\n\\|/\n |\n/ \\"

def append(list):
	list.append("Hello")
	print "List inside:",list
	return

printme("Hello, world!")
printthree("A different statement. ")
print_hangman()

mylist = ["hangman", "python", "ice cream"]
print "List before:",mylist
append(mylist)
print "List after:",mylist


def printnums():
	#num1 = 5
	#num2 = 10
	print "Addition:",num1+num2
	print "Multiplication:",num1*num2
	return

num1 = 15
num2 = 20
printnums()
print num1