#!/usr/bin/env python3

from sys import stdin

for line in stdin:
    lst = []
    line = list(map(int, line.strip().split()))
    if line[0] == line[1] == 0:
        break
    for _ in range(line[0]):
        lst.append(list(input()))
        #print("".join(ch for ch in sorted(list(input()), key=lambda c: c.casefold())))
    lst_transpose = list(sorted(list(map(list, zip(*lst))), key=lambda s: "".join(s).casefold()))
    lst = list(map(list, zip(*lst_transpose)))
    print("\n".join("".join(l) for l in lst))
    