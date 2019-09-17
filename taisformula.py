#!/usr/bin/env python3

n = int(input())
offset, yVals = map(float, input().split())


for i in range(n-2):
    x, y = map(float, input().split())

    offset += (2 * y) if i % 2 == 0 else (4 * y)
# offset += float(input().split()[1])
input()

print(offset * (1/3))
