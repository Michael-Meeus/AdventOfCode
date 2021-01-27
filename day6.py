inputFile = []
orbits = 0
with open("day6.txt") as fp:
    for line in fp:
        inputFile.append(line[:-1])

# inputFile.reverse()
def getFirstElement(line):
    return line[:1]

def getSecondElement(line):
    return line[2:]

def getArguments(line):
    arg1 = getFirstElement(line)
    arg2 = getSecondElement(line)
    return (arg1,arg2)

def lookForOrbit(data):
    planet = data[0]
    global inputFile
    for line in inputFile:
        if planet == getSecondElement(line) or planet == "COM":
            global orbits
            orbits += 1
            args = getArguments(line)
            lookForOrbit(args)


for line in inputFile:
    args = getArguments(line)
    lookForOrbit(args)

print(orbits)