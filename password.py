#!/usr/bin/env python3

lst = []
prob = 0
for _ in range(int(input())):
    lst.append(float(input().split()[1]))
lst = sorted(lst, reverse=True)
#print(lst)
for i, e in enumerate(lst):
    prob += (i+1) * e
print(prob)