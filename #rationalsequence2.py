#!/usr/bin/env python3

tree = {0: [(1,1)], 1: [(1,2),(2,1)], 2: [(1,3),(3,2),(2,3),(3,1)]}
for i in range(2,11):
    temp = []
    old = tree[i]
    for l, r in old:
        pass