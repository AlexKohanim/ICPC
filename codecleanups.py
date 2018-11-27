#!/usr/bin/python3
total, d, bp, i = 0, 0, 0, 1
input()
lst = list(map(int, input().split()))
while i < 367:
    if d >= 20:
        d, bp = 0, 0
        total += 1
        i -= 1
        continue
    d += bp
    if i in lst:
        bp += 1
    i += 1
if d > 0:
    total += 1
print(total)
