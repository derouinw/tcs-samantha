from random import randint

def randomize_list(size):
	theList = []
	for i in range(size):
		theList.append(i)

	for i in range(size*3):
		firstIndex = randint(0,size-1)
		secondIndex = randint(0,size-1)

		theList[firstIndex], theList[secondIndex] = theList[secondIndex], theList[firstIndex]

	return theList

def insertion_sort(theList):
	sortedList = [theList[0]]
	# for each unsorted element
	for i in range(1,len(theList)):
		element = theList[i]
		# check the sorted list
		pos = len(sortedList)
		for j in xrange(len(sortedList)):
			if (element < sortedList[j]):
				pos = j
				break
		sortedList.insert(pos, element)
	return sortedList

myList = randomize_list(10)
print myList
myList = insertion_sort(myList)
print myList