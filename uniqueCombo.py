#!/usr/bin/env python3
import itertools
def to_Proccess(iterables):
    return (list(tup) for tup in itertools.permutations(*iterables,))

print(list(to_Proccess([[1,2,3,4]])))
print(list(to_Proccess([[1,2,3] , [4,5,6]])))
print(list(to_Proccess([[1,2],[3,4],[5,6],[7,8]])))