#!/usr/bin/python3
"""This problem seems doable"""
import re
mirko_string = input()
explosion_string = input()
while explosion_string in mirko_string:
    #mirko_string = mirko_string.replace(explosion_string, "")
    mirko_string = re.sub(explosion_string, "", mirko_string)
if mirko_string == "":
    print("FRULA")
else:
    print(mirko_string)
#print("FRULA" if mirko_string == "" else mirko_string)
