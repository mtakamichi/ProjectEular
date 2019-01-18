#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 37
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
'''
from itertools import takewhile

def is_prime(n):
    if (n%2 == 0 and n>2) or n<=1:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    tnl, rnl = [], []
    lnl = list(str(n))
    for _ in range(len(lnl)-1):
        rnl.append(lnl.pop(0))
        tnl.extend([int(''.join(lnl)), int(''.join(rnl))])
    return all(map(is_prime, tnl))

nl = []
i = 11
while True:
    if is_truncatable_prime(i):
        nl.append(i)
    if len(nl) == 11:
        break
    i += 1
print(nl)
