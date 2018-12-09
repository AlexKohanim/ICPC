#!/usr/bin/env python3

t = int(input())
for _ in  range(t):
    d, m = map(int, input().split())
    count = 0
    offset_counter = 0
    for days in list(map(int, input().split())):
        if days >= 13 and offset_counter % 7 == 0:
            count += 1
        offset_counter += days % 7
        #print("offset_counter:", offset_counter)
    print(count)
