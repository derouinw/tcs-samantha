import glob
from random import randint

files = glob.glob("*.py")

num = randint(0,len(files)-1)

print files[num]

#lower = 0
#upper = len(files)-1
#num = randint(lower,upper)