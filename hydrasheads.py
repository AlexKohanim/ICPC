#!/usr/bin/env python3

from sys import stdin
# h+0 t+1
# h+1 t-2
# h-2 t+0

# goal, make h even and t == 0

for line in stdin:
    h, t = map(int, line.strip().split())
    if h == t == 0:
        break
    count = 0
    if h % 2 == 0:
        while t % 4 != 0:
            t+= 1
            count += 1
    else:
        while t % 4 == 0 or t % 2 != 0:
            t+= 1
            count += 1
    count += t // 2
    h += t // 2
    t = 0
    count += h // 2
    h = 0
    print(count)



