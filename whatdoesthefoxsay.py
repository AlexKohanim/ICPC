#!/usr/bin/env python3

t = int(input())
for _ in range(t):
    recordings = input().split()
    done = False
    while not done:
        line = input().split()
        if len(line) > 3:
            done = True
            break
        recordings = list(filter(lambda x: x != line[2], recordings))
    print(" ".join(recordings))