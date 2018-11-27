#!/usr/bin/env python3

def weak(n, e):
    for i in e[n]:
        if i != n:
            for k in e[n]:
                if n in e[k] and k != n and k != i:
                    return False
    return True
    
def itterate(v):
    e = dict()
    w = []
    for n in range(v):
        d = dict()
        j = input().split()
        print(j)
        # print(i,j)
        if j[1] == "1":
            d[0] = None
        e[n] = d
    for i in range(v):
        if weak(i, e):
            w.append(i)
    for i in range(len(w)):
        if i == len(w) - 1:
            print(w[i], end="")
        else:
            print(w[i], end = " ")
    print()

while True:
    i = int(input())
    if i < 0:
        break
    itterate(i)         
