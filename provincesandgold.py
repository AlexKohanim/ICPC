#!/usr/bin/env python3

gp = 3
sp = 2
cp = 1

gc = 6
sc = 3
cc = 0

pc = 8
dc = 5
ec = 2


g, s, c = map(int, input().split())

totalPower = g*gp + s*sp + c*cp
gotVictory = False
if totalPower >= pc:
    print("Province", end="")
    #totalPower -= pc
    gotVictory = True
if totalPower >= dc and not gotVictory:
    print("Duchy", end="")
    #totalPower -= dc
    gotVictory = True
if totalPower >= ec and not gotVictory:
    print("Estate", end="")
    #totalPower -= ec
    gotVictory = True
if gotVictory:
    print(" or ", end="")
if totalPower >= gc:
    print("Gold")
elif totalPower >= sc:
    print("Silver")
else:
    print("Copper")        

