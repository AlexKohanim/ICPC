#!/usr/bin/env python3
def toDigits(n, b):
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b 
    return digits

def fromDigits(digits, b):
    n = 0 
    for d in digits:
        n = b * n + d 
    return n

def convertBase(digits, b, c):
    return toDigits(fromDigits(digits, b), c)

n = input()
oc = 1 if len(n) % 3 == 2 else 0
oc = 2 if len(n) % 3 == 1 else oc
n = "0"*oc + n
#print(n)
#for i in range(0,len(n)-2,3):
#    print(convertBase([int(n[i]), int(n[i+1]), int(n[i+2])], 2, 8), end="")

[print(i, end="") for i in convertBase(list(map(int, n)), 2, 8)]
