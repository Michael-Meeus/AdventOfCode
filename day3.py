import math;

with open("day3.txt") as fp: 
    oneLine = fp.readline()
    twoLine = fp.readline()

field = [["." for x in range(30000)] for y in range(30000)] 
middleX = 15000
middleY = 15000
centralport = field[middleX][middleY]
oneLine = str.split(oneLine,",")
twoLine = str.split(twoLine,",")
oneSteps = []
twoSteps = []
crossings = []

def draw(line, symbol, nr):
    print("starting")
    x = middleX
    y = middleY
    steps = 0
    global field
    global oneSteps
    global twoSteps
    for i in range(len(line)):
        dir = line[i][:1]
        dis = int(line[i][1:])
        
        if dir == "U":
            for k in range(dis):
                x = x-1
                if field[x][y] != symbol and field[x][y] != ".":
                    field[x][y] = "#"
                    # if (nr == 1):
                    #     oneSteps = steps
                    # if (nr == 2):
                    #     twoSteps = steps
                    # print(steps)
                    # return
                    crossings.append((x,y))
                if field[x][y] == ".":
                    field[x][y] = symbol
                    steps+=1

        if dir == "R":
            for k in range(dis):
                y = y+1
                if field[x][y] != symbol and field[x][y] != ".":
                    crossings.append((x,y))
                    field[x][y] = "#"
                    # if (nr == 1):
                    #     oneSteps = steps
                    # if (nr == 2):
                    #     twoSteps = steps
                    # print(steps)
                    # return

                if field[x][y] == ".":
                    steps+=1
                    field[x][y] = symbol

        if dir == "D":
            for k in range(dis):
                x = x+1
                if field[x][y] != symbol and field[x][y] != ".":
                    crossings.append((x,y))
                    field[x][y] = "#"
                    # if (nr == 1):
                    #     oneSteps = steps
                    # if (nr == 2):
                    #     twoSteps = steps
                    # print(steps)
                    # return
                if field[x][y] == ".":
                    steps+=1
                    field[x][y] = symbol

        if dir ==  "L":
            for k in range(dis):
                y = y-1
                if field[x][y] != symbol and field[x][y] != ".":
                    crossings.append((x,y))
                    field[x][y] = "#"
                    # if (nr == 1):
                    #     oneSteps = steps
                    # if (nr == 2):
                    #     twoSteps = steps
                    # print(steps)
                    # return
                if field[x][y] == ".":
                    steps+=1
                    field[x][y] = symbol

    # print(oneSteps)
    # print(twoSteps)
    


draw(oneLine, "1", 1)
draw(twoLine, "2", 2)

# resultDistance = 9999999
# for crossing in crossings:
#     pythDistance = abs(middleX - crossing[0]) + abs(middleY - crossing[1])
#     if(pythDistance < resultDistance):
#         resultDistance = pythDistance


def search(line, symbol, nr):
    print("starting")
    x = middleX
    y = middleY
    steps = 0
    global field
    global oneSteps
    global twoSteps
    for i in range(len(line)):
        dir = line[i][:1]
        dis = int(line[i][1:])
        
        if dir == "U":
            for k in range(dis):
                x = x-1
                steps+=1
                if field[x][y] == "#":
                    if (nr == 1):
                        oneSteps.append(steps)
                    if (nr == 2):
                        twoSteps.append(steps)
                    # print(steps)
                    # return
                    
                

        if dir == "R":
            for k in range(dis):
                steps+=1
                y = y+1
                if field[x][y] == "#":
                    
                    if (nr == 1):
                        oneSteps.append(steps)
                    if (nr == 2):
                        twoSteps.append(steps)
                    # print(steps)
                    # return

            

        if dir == "D":
            for k in range(dis):
                steps+=1
                x = x+1
                if field[x][y] == "#":
                    
                    if (nr == 1):
                        oneSteps.append(steps)
                    if (nr == 2):
                        twoSteps.append(steps)
                    # print(steps)
                    # return
                

        if dir ==  "L":
            for k in range(dis):
                steps+=1
                y = y-1
                if field[x][y] == "#":
                    
                    if (nr == 1):
                        oneSteps.append(steps)
                    if (nr == 2):
                        twoSteps.append(steps)
                    # print(steps)
                    # return
                
# search(oneLine, "1", 1)
# search(twoLine, "2", 2)
# print(crossings)
# print(oneSteps)
# print(twoSteps)
print(field)