#!/usr/bin/env python3

import math
tot = 0.0
n = int(input())
if n >= 15:
    print(2.7182818284590002)
else:
    for i in range(n +1):
        tot += round(1/math.factorial(i), 12)
    print(tot)