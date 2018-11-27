from itertools import count, islice, takewhile
def primes(earlier_primes=[2, 3]):
    """Generate the prime numbers.

    >>> list(islice(primes(), 10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    """
    yield from earlier_primes
    for n in count(earlier_primes[-1] + 2, 2):
        if all(n % p for p in takewhile(lambda p: p**2 <= n, primes())):
            earlier_primes.append(n)
            yield n

lst = list(islice(primes(), 100000))
with open("primes.txt", "w") as file1:
    file1.write(str(dict(enumerate(lst))))
#print(d)
##for _ in range(int(input())):
##    l, u = map(int, input().split())
##    for i, e in enumerate(lst):
##        if e >= l:
##            l = i
##            break
##        
##    for x in lst[l:]:
##        if x > u:
##            break
##        print(x)
##    print()
