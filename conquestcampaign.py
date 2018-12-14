#!/usr/bin/env python3
import math

# I don't know this one..

r, c, n = map(int, input().split())
inital_pos = set()
for _ in range(n):
    inital_pos.add(tuple(map(int, input().split())))

distances = []
mapping = dict()
for x, y in inital_pos:
    distances.append(math.sqrt((1-x)**2 + (1-y)**2))
    distances.append(math.sqrt((1-x)**2 + (c-y)**2))
    distances.append(math.sqrt((r-x)**2 + (1-y)**2))
    distances.append(math.sqrt((r-x)**2 + (c-y)**2))

for i,d in enumerate(distances):
    mapping[i] = d


distances = sorted(distances)
print(distances)
print(mapping)



#print(table)