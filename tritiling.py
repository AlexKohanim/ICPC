#!/usr/bin/python3
"""The Problem that I hate"""
from sys import stdin

LST_A, LST_B = [1, 0], [0, 1]
LST_A.extend([0]*29)
LST_B.extend([0]*29)

for i in range(2, 31):
    LST_A[i] = LST_A[i - 2] + 2*LST_B[i - 1]
    LST_B[i] = LST_A[i - 1] + LST_B[i - 2]

for line in stdin:
    line = int(line.strip())
    if line < 0:
        break
    print(0 if line % 2 == 1 else LST_A[line] + LST_B[line])
