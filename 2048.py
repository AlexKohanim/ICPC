#!/usr/bin/env python3
#left, up, right, down
#0, 1, 2, 3

# This problem is not finished as of 11/27/18
l = []
for _ in range(4):
    l.append(list(map(int, input().split())))



def move(lst, d):
    if d == 0:
        for i in range(4):
            for j in range(1,4):
                if lst[i][3-j] == lst[i][3-j+1]:
                    lst[i][3-j+1] *= 2
                    lst[i][3-j] = 0
                elif lst[i][3-j+1] == 0:
                    lst[i][3-j+1] = lst[i][3-j]
                    lst[i][3-j] = 0
            print(lst[i])
            
                
    
move(l,int(input()))
