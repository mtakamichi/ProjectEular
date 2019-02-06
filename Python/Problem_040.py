#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 40
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
from functools import reduce
from operator import mul
def digits_of_Champernowne(nl):
    Champ = ' '
    for i in range(1, max(nl)):
        Champ += str(i)
    return [int(Champ[i]) for i in nl] 

dlist = digits_of_Champernowne([1, 10, 100, 1000, 10000, 100000])
print(reduce(mul, dlist))