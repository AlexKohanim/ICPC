#!/usr/bin/env python3

n = int(input())
trees = list(sorted(map(int, input().split()), reverse=True))
days = 0

for i, s in enumerate(trees):
    days = max(days, s+i+2)
print(days)
