#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import math

N=2000000
nl=range(2,N)
ind=0
latest_prime=2
while(latest_prime<math.sqrt(N)):
    nl = list(filter(lambda z: z%latest_prime!=0 or z==latest_prime, nl))
    latest_prime=nl[ind]
    ind+=1

print(sum(nl))
