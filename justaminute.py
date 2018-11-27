l = []
for _ in range(int(input())):
    r, a = map(int, input().split())
    l.extend([a/(r*60)]*r)
sl = sum(l)/float(len(l))
if sl <= 1.0:
    print("measurement error")
else:
    print(sum(l)/float(len(l)))
