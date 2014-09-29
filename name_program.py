def acronym(name):
	"takes the first latter of your name and prints them out"
	name_copy = name 
	result = name_copy[0]
	found = name_copy.find(" ")
	while found != -1:
		result += name_copy[found+1]
		name_copy = name_copy[found+1:]
		found = name_copy.find(" ")

	print result

def your_name_backwards(name):
	"takes your name and prints it backwards"
	result = ""
	# method 1: print backwards
	for i in range(len(name)-1, -1, -1):
		result += name[i]

	print result


	
print "What is your full name "
name = raw_input()

input = ""
while input != "4":
	print "1.acronym "
	print "2. your name backwards"
	print "3. words that start with your name"
	print "4. quit"
	input = raw_input("pick a number")

	if input == "1":
		acronym(name)
	elif input == "2":
		your_name_backwards(name)
	elif input == "3":
		words_that_start_with_your_name(name)
	elif input == "4":
		print "thanks for visiting name.py"
