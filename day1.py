import math
fuel = 0
totalFuel = 0
mass = 0

def calc(mass):
    mass = int(mass)
    mass = mass / 3
    mass = math.trunc(mass)
    mass = mass - 2
    if (mass > 0):
        global fuel
        fuel += mass
        calc(mass)
    return mass

with open("day1_input.txt") as fp:
    for line in fp:
        fuel = 0
        calc(line)
        totalFuel+=fuel
    print(totalFuel)
