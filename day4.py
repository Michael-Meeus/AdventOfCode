number = 172851
result = []
while(number != 675869):
    number+=1
    numberstring = str(number)
    a = numberstring[0]
    b = numberstring[1]
    c = numberstring[2]
    d = numberstring[3]
    e = numberstring[4]
    f = numberstring[5]
    if (int(a) <= int(b) and int(b) <= int(c) and int(c) <= int(d) and int(d) <= int(e) and int(e) <= int(f)):
        if (((int(a) == int(b)) and (int(a) != int(c))) or ((int(b) == int(c)) and (int(b) != int(d)) and (int(b) != int(a))) or ((int(c) == int(d)) and (int(c) != int(e)) and (int(c) != int(b))) or ((int(d) == int(e)) and (int(d) != int(f)) and (int(d) != int(c))) or ((int(e) ==int(f)) and (int(e) != int(d)))):
            result.append(number)
print(len(result))