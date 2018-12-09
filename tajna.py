#!/usr/bin/env python3

message = input()
val = len(message)
factors = [(i, val // i) for i in range(1, int(val**0.5)+1) if val % i == 0]
i,j = factors[-1]
#print(i,j)
k = 0
l = 0
while l < val:
    if k >= val:
        k = (k+1) % val
    print(message[k], end="")
    l += 1
    k += i
print()