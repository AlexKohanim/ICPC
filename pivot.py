#!/usr/bin/env python3

def main():
    n = int(input())

    a = list(map(int, input().split()))
    maxn = 0
    left = []
    for i, e in enumerate(a):
        if e > maxn:
            maxn = e
        left.append(maxn)

    steps = 0

    minn = maxn
    for i in range(n-1, -1, -1):
        if a[i] < minn:
            minn = a[i]
        if minn == left[i]:
            steps += 1
    print(steps)
if __name__ == '__main__':
    main()