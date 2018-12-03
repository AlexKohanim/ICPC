#!/usr/bin/env python3

n = int(input())
baloons = sorted(list(map(int, input().split()))) # might need to not sort, let's see
filled = 0
ratios = []
for i, b in enumerate(baloons):
    if b/(i+1) > 1:
        print("impossible")
        break
    ratios.append(b/(i+1))
else:
    print(round(min(ratios), 6))
