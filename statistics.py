from sys import stdin
for case, line in enumerate(stdin):
    line = line.strip()
    if len(line) == 0:
        break
    vals = list(map(int, line.split()))[1:]
    print("Case" , str(case+1) + ":", min(vals), max(vals), max(vals) - min(vals) )
    
