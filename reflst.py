lst2 = []
def reflist(lst):
    for l in lst:
        if type(l) is list:
            reflist(l)
        else:
            lst2.append(l)
    return lst2

print(reflist(['a',['b','c','d'],'e', ['f',['g',['h']]],'i']))
