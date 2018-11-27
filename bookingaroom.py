r, n = map(int, input().split())
if r == n:
    print("too late")
else:
    l = list(range(1, r+1))
    for _ in range(n):
        l.remove(int(input()))
    print(l[0])
