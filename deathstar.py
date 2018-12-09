#!/usr/bin/env python3

n = int(input())
matrix = []
array = [0]*n
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i != j:
            array[i] |= matrix[i][j]
            array[j] |= matrix[i][j]
print(" ".join(str(i) for i in array))
