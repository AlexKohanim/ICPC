#!/usr/bin/env python3
for _ in range(int(input())):
    message = input()
    k = len(message)
    while k**.5 != int(k**0.5):
        k += 1
    message += "*"*(k-len(message))
    start = k -int(k**0.5)
    for __ in range(k):
        if start < 0:
            start += k + 1
        if message[start] != "*":
            print(message[start], end = "")
        start -= int(k**0.5)
    print()


