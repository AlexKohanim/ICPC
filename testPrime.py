#!/usr/bin/env python3
import time

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True

def is_prime2(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i < int(num**0.5):
        if num % i == 0:
            return False
        i += 1
    return True

start = time.time()
n = 2**(82589933) -1
res = is_prime(n)
print(res, "elapsed", time.time() - start)
start = time.time()
is_prime2(n)
print(res, "elapsed", time.time() - start)