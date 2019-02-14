#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 27
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
'''

def is_prime(n):
    if (n%2 == 0 and n>2) or n<=1:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

def len_quad_prime(a, b):
    n=0
    while(is_prime(n**2 + a*n + b)):
        n+=1
    return max(n-1, 0)

al = list(range(-1000,1000))
bl = list(filter(is_prime, range(1, 1000)))
lqpl = [len_quad_prime(a,b) for a in al for b in bl]
abl = [a*b for a in al for b in bl]

print(abl[lqpl.index(max(lqpl))])
