for _ in range(int(input())):
    lst = []
    for __ in range(int(input())):
        lst.append(input())
    lst = sorted(lst, key=len, reverse=True)
    mash = set()
    for l in lst:
        if l in mash:
            print("NO")
            break
        for i in range(1, len(l)+1):
            mash.add(l[:i])
    else:
        print("YES")
