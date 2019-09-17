#!/usr/bin/env python3

n, q = map(int, input().split())
X = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        X[query[1]-1] = query[2]
    else:
        print(abs(X[query[2]-1] - X[query[1]-1]))
