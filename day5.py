initInput = [3,225,1,225,6,6,1100,1,238,225,104,0,1002,92,42,224,1001,224,-3444,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1102,24,81,225,1101,89,36,224,101,-125,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,118,191,224,101,-880,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,68,94,225,1101,85,91,225,1102,91,82,225,1102,85,77,224,101,-6545,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,84,20,225,102,41,36,224,101,-3321,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1,188,88,224,101,-183,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1001,84,43,224,1001,224,-137,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1102,71,92,225,1101,44,50,225,1102,29,47,225,101,7,195,224,101,-36,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,374,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,389,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,434,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,226,226,224,102,2,223,223,1006,224,494,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,524,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,584,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,614,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,7,677,677,224,102,2,223,223,1005,224,644,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,659,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

index0 = 0 #input[0]
index1 = 1 #input[1]
index2 = 2 #input[2]
index3 = 3 #input[3]
modified = False
result = 0
number1 = 0
number2 = 0
output = []

def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def save(position):
    global initInput
    print("Enter your input: ")
    integer = input() 
    initInput[position] = int(integer)

def output(position):
    if(initInput[position] != 0):
        print("failed")
    print(initInput[position])

def getIntcode():
    if len(str(initInput[index0]))>1:
        intcode = int(str(initInput[index0])[-2:])
    else:
        intcode = initInput[index0]
    return intcode

def getFirst():
    if len(str(initInput[index0]))>2:
        if len(str(initInput[index0]))==3:
            return int(str(initInput[index0])[0])
        if len(str(initInput[index0]))==4:
            return int(str(initInput[index0])[1])
    return 0
    
def getSecond():
    if len(str(initInput[index0]))>2:
        if len(str(initInput[index0]))==3:
            return 0
        if len(str(initInput[index0]))==4:
            return int(str(initInput[index0])[0])
    return 0

def jump_if_true(param1, param2):
    global index0
    global index1
    global index2
    global index3
    global modified
    
    if param1!=0:
        modified = True
        index0 = param2
        index1 = index0 + 1
        index2 = index0 + 2
        index3 = index0 + 3

def jump_if_false(param1, param2):
    global index0
    global index1
    global index2
    global index3
    global modified
    
    if param1==0:
        modified = True
        index0 = param2
        index1 = index0 + 1
        index2 = index0 + 2
        index3 = index0 + 3

def less(param1, param2):
    if param1<param2:
        initInput[initInput[index3]] = 1
    else:
        initInput[initInput[index3]] = 0
        #TODO: increase nest

def equals(param1, param2):
    if param1==param2:
        initInput[initInput[index3]] = 1
    else:
        initInput[initInput[index3]] = 0
        #TODO: increase nest

def advance(x):
    global index0
    global index1
    global index2
    global index3
    index0+=x
    index1+=x
    index2+=x
    index3+=x

intcode = getIntcode()
firstMode = getFirst()
secondMode = getSecond()

while intcode!=99 and intcode!="99":

    if intcode == 1 or intcode == "01":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[initInput[index1]]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        result = add(number1, number2)
        initInput[initInput[index3]] = result
        advance(4)
    elif intcode == 2 or intcode == "02":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[initInput[index1]]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        result = mul(number1, number2)
        initInput[initInput[index3]] = result
        advance(4)
    elif intcode == 3 or intcode == "03":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[index1]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        result = save(number1)
        advance(2)
    elif intcode == 4 or intcode == "04":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[index1]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        result = output(number1)
        advance(2)
    elif intcode == 5 or intcode == "05":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[initInput[index1]]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        jump_if_true(number1, number2)
        if modified!=True:
            advance(3)
        modified=False

    elif intcode == 6 or intcode == "06":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[initInput[index1]]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        jump_if_false(number1, number2)
        if modified!=True:
            advance(3)
        modified=False

    elif intcode == 7 or intcode == "07":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[initInput[index1]]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        less(number1, number2)
        advance(4)

    elif intcode == 8 or intcode == "08":
        try:
            if (firstMode == 0 or firstMode == "0"):
                number1 = initInput[initInput[index1]]
            if (firstMode == 1 or firstMode == "1"):
                number1 = initInput[index1]
        except:
            number1 = 0
        try:
            if (secondMode == 0 or secondMode == "0"):
                number2 = initInput[initInput[index2]]
            if (secondMode == 1 or secondMode == "1"):
                number2 = initInput[index2]
        except:
            number2 = 0
        equals(number1, number2)
        advance(4)


    intcode = getIntcode()
    firstMode = getFirst()
    secondMode = getSecond()
    

index0 = 0
index1 = 1
index2 = 2
index3 = 3
result = 0
number1 = 0
number2 = 0
