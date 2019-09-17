#!/usr/bin/env python3

input()

print(sum([abs(num) for num in list(map(int, input().split())) if num < 0]))