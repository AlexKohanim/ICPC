#!/usr/bin/env python3.5
from sys import stdin
d = {0:0, 1:1, 2:2}

def recFunc(n):
    if n in d:
        return d[n]
    #print(n, n//2, n//3, n//4)
    d[n] = max(n, recFunc(n//2) + recFunc(n//3) + recFunc(n//4))
    return d[n]

 

for line in stdin:
    line = line.strip()
    if len(line) == 0:
        break
    recFunc(int(line))
    print(d[int(line)])
    #print(sorted(d.items()))
        
