from sys import stdin
for line in stdin:
    line = line.strip()
    if len(line) == 0:
        break    
    vals = line.split()
    name = []
    total, num = 0.0, 0.0
    for v in vals:
        if v.split(".")[0].isdigit():
            total += float(v)
            num += 1
        else:
            name.append(v)

    print("%.6f"%round(total/num, 6), end = " ")
    print(" ".join(n for n in name))
