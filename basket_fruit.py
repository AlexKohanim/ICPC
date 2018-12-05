#!/usr/bin/python3
"""Problem Description"""

def solution(tree_array):
    """Function that counts fruit"""
    if len(tree_array) == 1:
        return 1
    total, r_pos, count, l_val, r_val = 2, 1, 2, tree_array[0], tree_array[1]
    while r_pos < len(tree_array) -1:
        if tree_array[r_pos +1] != l_val and tree_array[r_pos +1] != r_val:
            total = count if count > total else total
            count = 2
            r_pos += 1
            l_val, r_val = r_val, tree_array[r_pos]
        else:
            count += 1
            r_pos += 1

    return max(total, count)

print(solution(list(map(int, input().split()))))
