#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 35
How many circular primes are there below one million?
'''
def is_prime(n):
    if (n%2 == 0 and n>2) or n<=1:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

def is_circ_prime(n):
    cnl = []
    nl = list(str(n))
    for _ in range(len(nl)-1):
        nl.append(nl.pop(0))
        cnl.append(int(''.join(nl)))
    return all(map(is_prime, cnl))

print(list(map(is_circ_prime, filter(is_prime, range(2, 1_000_000)))).count(True))
