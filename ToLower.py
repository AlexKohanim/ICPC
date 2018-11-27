p, t = map(int, input().split())
c = 0
for i in range(p):
    found = True
    for j in range(t):
        s = input()
        if not s[1:].islower():
            found = False
    if found:
        c += 1
print(c)
