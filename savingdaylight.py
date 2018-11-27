from sys import stdin
import datetime

for line in stdin:
    if(len(line) < 3):
        break
    m, d, y, s, e = line.split()
    t1 = datetime.datetime.strptime(s, '%H:%M')
    t2 = datetime.datetime.strptime(e, '%H:%M')
    
    hours = t2 - t1
    tc = str(hours).split(":")
    print(m,d,y,tc[0] + " hours",  int(tc[1]),  "minutes")
