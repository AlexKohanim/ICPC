from sys import stdin
for line in stdin:
    line = line.strip()
    if len(line) == 0:
        break
    lst = list(map(int, line.split()))
    total = sum(lst)
    for item in lst:
        if total - item == item:
            print(item)
            break
