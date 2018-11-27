from sys import stdin
case_num = 1
for line in stdin:
    line = line.strip()
    if len(line) == 0:
        break
    day_count = 0
    e, m = map(int, line.split())
    while not (e % 365 == 0 and m % 687 == 0):
        e += 1
        m += 1
        day_count +=1
    print("Case "+ str(case_num), day_count, sep = ": ")
    case_num += 1
    
    
