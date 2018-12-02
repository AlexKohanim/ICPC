#!/usr/bin/env python3

for i in range(int(input())):
    print(i+1, end=" " )
    n = int(input().split()[1])+1
    print(((n*(n+1))//2)-1)
    