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
        n = b * n + int(d)
    return n

def convertBase(digits, b, c):
    return toDigits(fromDigits(digits, b), c)

for n in range(int(input())):
    print(n+1, end=" ")
    line = input().split()
    newBase = convertBase(line[2], 10, int(line[1]))
    print(sum([i**2 for i in newBase]))

