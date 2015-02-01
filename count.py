import glob
import operator

files = glob.glob("*.py")
files2 = glob.glob("game/*.py")
for f in files2:
	files.append(f)

linecount = 0
filecounts = {}
for filename in files:
	f = open(filename, "r")
	lines = f.read().split("\n")
	linescount = len(lines)
	linecount += linescount
	filecounts[filename] = linescount

sorted_d = sorted(filecounts.items(), key=operator.itemgetter(1))

for d in sorted_d:
	print d[0] + ": " + str(d[1])

print linecount