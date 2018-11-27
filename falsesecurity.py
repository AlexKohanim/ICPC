#!/usr/bin/env python3
import sys
letters = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ".": "---.",
    ",": ".-.-",
    "?": "----"
}

inv_letters = {}

for l in letters:
    inv_letters[letters[l]] = l

for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    counts, p = [], ""
    for c in line:
        m = letters[c]
        p += m
        counts.append(len(m))
    counts.reverse()
    ti = 0
    out = ""
    for c in counts:
        out += inv_letters[p[ti:ti+c]]
        ti += c
    print(out)
    
