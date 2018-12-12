
#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 14
Longest Collatz sequence
'''
from functools import lru_cache

@lru_cache(maxsize=1000000)
def Collatz(n):
    if(n<=1):
        return 1
    elif(n%2==0):
        return 1+Collatz(int(n/2))
    else:
        return 1+Collatz(int(3*n+1))

cl = list(map(Collatz, range(0,1000000)))
print(cl.index(max(cl)))
print(max(cl))
