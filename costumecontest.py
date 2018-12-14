#!/usr/bin/env python3

from collections import Counter

lst = [input() for _ in range(int(input()))]

com = Counter(lst).most_common()

n = com[-1][1]
out = []
for i in range(len(com)-1,-1,-1):
    if com[i][1] == n:
        out.append(com[i][0])
print("\n".join(c for c in sorted(out)))