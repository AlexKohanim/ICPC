#!/usr/bin/env python3
from sys import stdin
import sys
sys.setrecursionlimit(999999999)
def visit(r, c, mr, mc, s):
    s[r][c] = "#"
    if r-1 >= 0 and s[r-1][c] == '-':
        visit(r-1, c, mr, mc, s)
    if r+1 <= mr and s[r+1][c] == '-':
        visit(r+1, c, mr, mc, s);
    if c-1 >=0 and s[r][c-1] == '-':
        visit(r, c-1, mr, mc, s);
    if c+1 <= mc and s[r][c+1] == '-':
        visit(r, c+1, mr, mc, s);

cn = 0
while True:
    try:
        line = stdin.readline()
    except KeyboardInterrupt:
        break

    if not line or len(line.strip()) == 0:
        break
    s = []
    line = list(map(int, line.split()))
    cn, sc = cn + 1, 0
    n, m = line[0], line[1]
    for _ in range(n):
        s.append(list(input()))
    for r in range(n):
        for c in range(m):
            if s[r][c] == "-":
                sc += 1
                visit(r, c, n-1, m-1, s)
    print("Case " + str(cn), sc, sep=": ")    

