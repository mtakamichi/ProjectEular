#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 33
If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
'''
from math import gcd

nprod, dprod = 1, 1
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            numera = i*10 + k
            denomi = j + 10*k
            if numera < denomi and numera*j == denomi*i:
                nprod *= numera
                dprod *= denomi

print(dprod//gcd(nprod, dprod))