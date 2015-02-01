title = ""
rooms = []
titles = []
while title != "end":
	print("Enter title: ")
	prev = title
	title = raw_input()
	print("Enter text: ")
	text = raw_input()
	print("Enter valid input: ")
	valid = raw_input()

	rooms.append("[" + title + "]\ntitle: " + title + "\nopening_message: " + text + "\nvalid_input: " + valid + "\n")
	titles.append(title)

fileout = open("rooms.txt", "a")
titlesout = open("section_names.txt", "a")
for i in range(len(rooms)):
	room = rooms[i]
	if "[end]" not in room:
		fileout.write(room)
		fileout.write("next_room: " + titles[i+1] + "\n\n") # rooms[i+1][1:rooms[i+1].find("]")]
	else:
		fileout.write(room)
		fileout.write("next_room: end")
	titlesout.write(titles[i]+"\n")

fileout.close()
titlesout.close()

print("done!")