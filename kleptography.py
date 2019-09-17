#!/usr/bin/env python3

k_length, e_length = map(int, input().split())

stored_key = list(input())
plain_text = list(input())

stored_key += " "*(e_length - k_length)

for i in range(len(stored_key)):
    plain_text[i] = chr(((ord(plain_text[i]) + ord(stored_key[i])) % 26) + ord('a')-1)
print(plain_text)

# l -> n -2
# a -> i -8
# o -> a 14
# t -> g 13
# s -> a 18



