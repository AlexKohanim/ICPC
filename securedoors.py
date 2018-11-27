l = []
for _ in range(int(input())):
    t, p = input().split()
    if t == "entry":
        if p in l:
            print(p, "entered (ANOMALY)")
        else:
            print(p, "entered")
            l.append(p)
    else:
        if p not in l:
            print(p, "exited (ANOMALY)")
        else:
            print(p, "exited")
            l.remove(p)
