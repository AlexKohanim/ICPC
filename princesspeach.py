#!/usr/bin/env python3
n, y = map(int, input().split())
c = 1
lst = {int(input()) for _ in range(y)}
[print(i) for i in range(n) if i not in lst]
# for i in range(n):
#     if i == avoid and c < y:
#         avoid = int(input())
#         c += 1
#         continue
#     print(i)
print("Mario got", len(lst),"of the dangerous obstacles.")