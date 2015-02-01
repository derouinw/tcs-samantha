import ConfigParser

class Room:

	def __init__(self, title, opening_message, valid_input, next_room):
		self.title = title
		self.opening_message = opening_message
		self.valid_input = valid_input
		self.next_room = next_room

	def get_title(self):
		return self.title

	def get_message(self):
		return self.opening_message

	def get_input(self):
		return self.valid_input

	def check_input(self, input):
		return (input == self.valid_input)

	def get_next(self):
		return self.next_room

def display_message():
	print room.get_message()

def get_input():
	print ""
	input = raw_input("input: ")
	print ""
	return input

def process_input(input):
	if room.check_input(input):
		return room.get_next()
	elif input == "help":
		print room.get_input()
		print ""
		return room.get_title()
	else:
		print "invalid input"
		return room.get_title()

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

# Setup data
section_names_f = open("section_names.txt", 'r')
section_names = section_names_f.read().split("\n")
section_names_f.close();

rooms = {}

config = ConfigParser.ConfigParser()
config.read("rooms.txt")
for section in section_names:
	room = ConfigSectionMap(section)
	title = room['title']
	opening_message = room['opening_message']
	valid_input = room['valid_input']
	next_room = room['next_room']
	rooms[title] = Room(title, opening_message, valid_input, next_room)

# Setup game
room = rooms['start']
current_message = room.get_message()
playing = True

# Main game loop
while playing:
	if room.get_title() == "end":
		playing = False
	display_message()
	if not playing:
		break
	input = get_input()
	room = rooms[process_input(input)]

print "\n\nThanks for playing!"