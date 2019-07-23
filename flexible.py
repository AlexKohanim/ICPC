#!/usr/bin/env python3

w, n = map(int, input().split())
partitions = list(map(int, input().split()))
partitions.append(w)

out = set(partitions)
for i in range(n):
    for j in range(i+1,n+1):
        out.add(partitions[j] - partitions[i])

for o in sorted(out):
    print(o, end = " ")
print()