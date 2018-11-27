#!/usr/bin/env python3

def isHarshad(n):
    return n % sum([int(i) for i in list(str(n))]) == 0

n = int(input())
while not isHarshad(n):
    n += 1
print(n)