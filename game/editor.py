titles = []
texts = []
inputs = []

title = ""
incomplete = False

# get content from user
while title != "end":
	title = raw_input("Enter the title: ")
	text = raw_input("Enter the text: ")
	input = raw_input("Enter the input: ")

	if title == "end" and text == "end" and input == "end":
		incomplete = True

	titles.append(title)
	texts.append(text)
	inputs.append(input)

# write output files
dataout = open("rooms.txt", "a")
sectionsout = open("section_names.txt", "a")

for i in range(len(titles)):
	if (i != 0): 
		sectionsout.write("\n")
	sectionsout.write(titles[i])

	if incomplete and titles[i] == "end":
		break
	dataout.write("[" + titles[i] + "]\ntitle: " + titles[i] + "\n")
	dataout.write("opening_message: " + texts[i] + "\n")
	dataout.write("valid_input: " + inputs[i] + "\n")
	if (titles[i] != "end"):
		dataout.write("next_room: " + titles[i+1] + "\n\n")
	else:
		dataout.write("next_room: end")

dataout.close()
sectionsout.close()