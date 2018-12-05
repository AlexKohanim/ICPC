#!/usr/bin/share python3
""" this module does whatever"""
Target = int(input())
Vals = list(map(int, input().split()))
D = dict()
for i in range(len(Vals)):
    if Vals[i] in D:
        print(i, D[Vals[i]])
        break
    D[Target - Vals[i]] = i

