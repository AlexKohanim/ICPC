#!/usr/bin/env python3

d = dict()
sentences = []
queries = []

for i in range(int(input())):
    sentences.append(input().split())
    for word in sentences[-1]:
        if word in d:
            d[word].add(i)
        else:
            d[word] = {i}
#print(d)
for _ in range(int(input())):
    queries.append(input().split())
    tempSet = set()
    for i, querie in enumerate(queries[-1]):
        #print(tempSet)
        if i == 0:
            tempSet = d[querie]
            continue
        tempSet &= d[querie]
    print (" ".join(str(t) for t in tempSet))
