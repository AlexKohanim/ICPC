#!/usr/bin/env python3

dictionary = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "nmo", 7: "pqrs", 8: "tuv", 9: "wxyz"}
canidates = [input() for _ in range(int(input()))]
sequence = input()

for i, n in enumerate(sequence):
    for can in canidates:
        if can[i] not in dictionary[int(n)]:
            canidates.remove(can)
print(len(canidates))
