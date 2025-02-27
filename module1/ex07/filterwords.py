import sys
import string

line:str = ""

if len(sys.argv) != 3:
    print("ERROR")
    sys.exit()
try:
    nb = int(sys.argv[2])
except ValueError:
    print("ERROR")
    sys.exit()
line = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
lalist:list = line.split(' ')
finallist:list = []
for word in lalist:
    if len(word) >= nb:
        finallist.append(word)
print(finallist)