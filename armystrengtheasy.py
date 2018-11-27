#!/usr/bin/env python3.5

""" This code does stuff """
for _ in range (int(input())):
    input()
    input()
    godzilla = max([*map(int, input().split())])
    m_godzilla = max([*map(int, input().split())])
    #print(type(godzilla), type(m_godzilla))
    print("Godzilla" if godzilla >= m_godzilla else "MechaGodzilla")
