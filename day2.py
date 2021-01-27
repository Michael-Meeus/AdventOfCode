input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
initInput = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]

index0 = 0 #input[0]
index1 = 1 #input[1]
index2 = 2 #input[2]
index3 = 3 #input[3]
result = 0
number1 = 0
number2 = 0

end = 19690720
endresult = ""

def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def advance():
    global index0
    global index1
    global index2
    global index3
    index0+=4
    index1+=4
    index2+=4
    index3+=4

for i in range(100):
    for j in range(100):
        input[1] = i
        input[2] = j

        while input[index0]!=99:
            number1 = input[input[index1]]
            number2 = input[input[index2]]
            if input[index0] == 1:
                result = add(number1, number2)
            else:
                result = mul(number1, number2)

            input[input[index3]] = result
            advance()
        
        if input[0] == end:
            endresult = "i = "+i+"and j= "+j

        print(input[0])
        input = initInput
        index0 = 0
        index1 = 1
        index2 = 2
        index3 = 3
        result = 0
        number1 = 0
        number2 = 0

print(endresult)