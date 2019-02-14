#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 34
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
'''
from functools import reduce
from operator import add
from math import factorial

print(sum(filter(lambda x: x == reduce(add, map(factorial, list(map(int, list(str(x)))))), range(3, factorial(9)*7))))

""" ans = 0
for i in range(3, factorial(9)*7):
    nl = list(map(int, list(str(i))))
    if i == reduce(add, map(factorial, nl)):
        ans += i
print(ans)
 """