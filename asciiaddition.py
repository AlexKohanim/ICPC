#!/usr/bin/python3
"""A simple problem they say"""
ascii_holder = {"""xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx
""" : "0", """....x
....x
....x
....x
....x
....x
....x
""" : "1", """xxxxx
....x
....x
xxxxx
x....
x....
xxxxx
""" : "2", """xxxxx
....x
....x
xxxxx
....x
....x
xxxxx
""" : "3", """x...x
x...x
x...x
xxxxx
....x
....x
....x
""" : "4", """xxxxx
x....
x....
xxxxx
....x
....x
xxxxx
""" : "5", """xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx
""" : "6", """xxxxx
....x
....x
....x
....x
....x
....x
""" : "7", """xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx
""" : "8", """xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx
""" : "9", """.....
..x..
..x..
xxxxx
..x..
..x..
.....
""" : "+"}

#for k, v in ascii_holder.items():
    # print(k)

to_proccess = []
proccessing = ""
for _ in range(7):
    to_proccess.append(input())

for i in range(len(to_proccess[0]) - 5):
    comp_str = ""
    for j in range(7):
        comp_str += to_proccess[j][5*i + i:5*i+5+i] + "\n"
    if len(comp_str.strip("\n")) > 1:
        # print(comp_str)
        proccessing += ascii_holder[comp_str]

proccessed = eval(proccessing)

char_ascii = []
#print(proccessed)

for c in str(proccessed):
    for k, v in ascii_holder.items():
        if v == c:
            char_ascii.append(k)
            break
#print(char_ascii)
to_output = ""
for j in range(7):
    for i in range(len(str(proccessed))):
        to_output += char_ascii[i].split("\n")[j] + "."
    to_output = to_output[0:-1] + "\n"
print(to_output, end = "")
