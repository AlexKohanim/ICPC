import sys
from collections import OrderedDict
stocks=OrderedDict()
with open(sys.argv[1], 'r') as s:
    s.readline()
    for line in s.read().split("\n"):
        if (len(line) < 2):
            break
        the_key = line.split("-")
        date = the_key[0] + the_key[1]
        adj_close = float(line.split(",")[4])
        if date in stocks:
            stocks.update({date:adj_close})
        else:
            stocks[date] = float(line.split(",")[4])
for k,v in stocks.items():
    print(k,max(v),sep="\t")
        
