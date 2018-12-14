#!/usr/bin/env python3

for _ in range(int(input())):
    num = input()[::-1]
    tot = 0
    for  i, e in enumerate(list(num)):
        if i%2 == 1:
            temp = 2*int(e)
            if temp >9:
                temp = temp // 10 + temp %10
            tot += temp
        else:
            tot += int(e)
    print("FAIL" if tot %10 else "PASS")

