#!/usr/bin/env python3
l = []
m = []
for _ in range(9):
    l.append(int(input()))
tot = sum(l)
t = 0b001111111
s = 0
for i in range(8):
    for j in range(i+1,9):
        if j == i:
            continue
        if tot - l[i] - l[j] == 100:
            for k, x in enumerate(l):
                if k == i or k == j:
                    continue
                print(x)

