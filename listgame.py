#!/usr/bin/python3
"""A Doc String"""
from functools import reduce
from math import sqrt

def factors_small(n):
    """Better when number is smaller than 100"""
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def factors_big(n):
    """Better when bigger than 100"""
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

n = int(input())
if n < 100:
    s = factors_small(n)
    print(s)
else:
    s = factors_big(n)
    print(s)
