#!/usr/bin/env python3

#Not finished as of 12/9/18
totalset = {frozenset({0,1,2})}
for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1,12):
            totalset.add(frozenset({i,j,k}))
input_list = []
for i in range(4):
    input_list.extend(input().split())
#print(totalset)
for comb in totalset:
    comb = list(comb)
    #print(len(input_list))
    #print(comb)
    #To make a set, you must select three cards for which all 4 characteristics are either the same or pairwise different
    tempSet = set(input_list[comb[0]]) &  set(input_list[comb[1]]) & set(input_list[comb[2]])
    print(tempSet)
    if len(tempSet) == 3:
        print(" ".join(str(c+1) for c in sorted(comb)))
