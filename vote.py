#!/usr/bin/env python3

for _ in range(int(input())):
    lst = []
    for __ in range(int(input())):
        lst.append(int(input()))
    n = max(lst)
    if lst.count(n) > 1:
        print("no winner")
        continue
    winner = lst.index(n)
    out = "winner " + str(winner+1)
    print("majority "+out if n/sum(lst) > 0.5 else "minority "+out)