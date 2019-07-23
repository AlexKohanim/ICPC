#!/usr/bin/env python3

'''
1 -> 1/1
2 -> 1/2
3 -> 2/1
4 -> 1/3
5 ->

'''

for _ in range(int(input())):
    i, fract = input().split()
    p, q = map(int, fract.split("/"))

    offset_positions = [0]*max(p, q)
    offset_index = 0

    while (p is not q):
        if p > q:
            p -= q
            offset_positions[offset_index] = 0
        else:
            q -= p
            offset_positions[offset_index] = 1
        offset_index += 1

    level_and_offset_counter = 1
    offset_power_level = 0 if len(offset_positions) == 0 else int("".join(str(x) for x in offset_positions))

    for j in range(offset_index - 1, -1, -1):
        if offset_power_level and 2**j:
            level_and_offset_counter = (level_and_offset_counter << 1) + 1
        else:
            level_and_offset_counter = 2**level_and_offset_counter
    print(i, level_and_offset_counter)
