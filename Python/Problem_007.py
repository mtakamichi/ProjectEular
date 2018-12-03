#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
import math

# is_prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

p=2
count = 0
while(True):
    if is_prime(p):
        count+=1
    if count==10001:
        break
    p+=1
print(p)
