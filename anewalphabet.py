#!/usr/bin/env python3.5
""" This code does stuff """
a_convert = {'a': '@', 'b' : '8', 'c' : '(', 'd' : '|)', 'e' : '3', 'f' : '#', 'g' : '6', 'h' : '[-]' , 'i' : '|', 'j' : '_|', 'k' : '|<', 'l' : '1', 'm' : '[]\/[]', 'n' : '[]\[]', 'o' : '0', 'p' : '|D', 'q' : '(,)', 'r' : '|Z', 's' : '$', 't' : '\'][\'', 'u' : '|_|', 'v' : '\\/', 'w' : '\\/\\/', 'x' : '}{', 'y' : '`/', 'z' : '2' }
for c in input().lower():
    if c in a_convert:
        print(a_convert[c], end="")
    else:
        print(c, end="")
print()
