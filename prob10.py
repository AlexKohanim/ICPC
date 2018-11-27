#!/usr/bin/env python3
import sys
from operator import mul
from functools import reduce
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    line = line.split()
    if int(line[0]) == 1 or int(line[1]) == 1:
        print("bad")
        continue
    f1, f2 = prime_factors(int(line[0])), prime_factors(int(line[1]))
    a = f1 if len(f1) <= len(f2) else f2
    b = f2 if a == f1 else f1
    for p in a:
        if p in b:
            print ("bad")
            break
    else:
        a.extend(b)
        c = int(line[0]) + int(line[1])
        cp = prime_factors(c)
        a.extend(cp)
        d = reduce(mul, set(a), 1)
        if d == c:
            print('equals')
        else:
            print('less' if d < c else 'greater')
