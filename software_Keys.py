#!/usr/bin/python3

""" The program that does the stuff
Design a function which corrects software keys.

Function input is a string S and an integer K.
The string is a mix of upper and lowercase alphanumeric characters
partitioned with hyphens (possibly misplaced).
The function should return the string S partitioned to have exactly K
characters in each partition, except for possibly the first
one, and for the string to be all uppercase.
So given input S = '2Kr7-a1-3j' and K = 4, the function
should return '2KR7-A13J'. Given input S = 'r', K = 1, the
function should return 'R'. Given input S = '2Kr7-a1-3J`.
and K = 3, the function should return `2K-R7A-13J`.
You can assume that K is a positive integer >=

"""

def fix_keys(bad_key, k):
    """A Function doc string"""
    bad_key = bad_key.replace("-", "").upper()
    out_string = bad_key[0 : len(bad_key) % k] + "-" if len(bad_key) % k != 0 else ""
    out_string += "-".join([bad_key[i:i+k] for i in range(len(bad_key) % k, len(bad_key), k)])
    return out_string

print(fix_keys(input(), int(input())))
