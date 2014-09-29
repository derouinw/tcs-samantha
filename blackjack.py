from random import randint

def shuffle():
	for i in xrange(100):
		first = randint(0,51)
		second = randint(0,51)

		if first != second:
			deck[first], deck[second] = deck[second], deck[first] # python swapping is super easy!

deck = []

# Adds the cards
for card in xrange(1,14): # one for each number (A = 1, J,Q,K = 11, 12, 13)
    for suit in xrange(4): # 4 for each suit
		deck.append(card)

shuffle()

# let's play!
money = 100
wins = 0
losses = 0
bet = 0

while money > 0:
	print "You have", money, "dollars. What would you like to bet? (-1 = quit)"
	bet = int(raw_input("$"))

	if bet == -1:
		break

	if bet > money:
		print "You don't have that much money!"
		continue
	else:
		money = money - bet

	hit = True

	# draw the first card (haven't taught this so I left it)
	hand = deck.pop()
	deck.insert(0, hand)


	while hit and hand <= 21:
		print "Your hand is",hand,"Would you like to hit or stay?"
		option = raw_input("(1 = hit, 2 = stay)")
		if option == "1":
			# draw a new card
			new = deck.pop()
			hand = hand + new
			deck.insert(0, new)
		elif option == "2":
			hit = False
		else:
			print "That's not a valid choice"

		if hand > 21:
			print "You busted!"

	if hand <= 21:
		dealer = randint(1,22)
		print "The dealer has",dealer
		if hand > dealer:
			print "You won the hand!"
			money = money + 2 * bet
			wins = wins + 1
		else:
			print "You lost the hand"
			losses = losses + 1

	shuffle()

print "Game over"
print "You had",money,"dollars left"
print "You won",wins,"times"
print "You lost",losses,"times"