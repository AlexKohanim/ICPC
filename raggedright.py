#!/usr/bin/env python3

from sys import stdin

lst = []
for line in stdin:
    line = line.strip()
    lst.append(len(line))

n = max(lst)
tot = 0
for i in range(len(lst)-1):
    tot += (n-lst[i])**2
print(tot)