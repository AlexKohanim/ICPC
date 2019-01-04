#!/usr/bin/env python3

lst = [0]*366


for _ in range(int(input())):
    lower, upper = map(int, input().split())
    for i in range(lower,upper+1):
        if lst[i] == 0:
            lst[i] = 1
print(sum(lst))
