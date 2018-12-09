#!/usr/bin/env python3
from sys import stdin
d = {0:0, 1:1, 2:2}
for line in stdin:
    line = line.strip()
    if len(line) == 0:
        break
    n = int(line)
    if n in d.keys():
        print(d[n])
    else:
        d[n] = n + n -2
        print(d[n])