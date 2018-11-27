from sys import stdin
store = dict()
for line in stdin:
    line = line.strip()
    if(len(line) == 0):
        break
    line = line.split()
    store[line[1]] = line[0]

for line in stdin:
    line = line.strip()
    if(len(line) == 0):
        break
    if line in store.keys():
        print(store[line])
    else:
        print('eh')
