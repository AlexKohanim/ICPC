#!/usr/bin/env python3

import math
n = int(input())
a = [i for i in range(2,n+1)]
for i in range(int(math.sqrt(n))):
    if i in a:
        j = i * 2
        while j <= n:
            if j in a:
                a.remove(j)
            j += i
print(a)
