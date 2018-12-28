#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 20
Find the sum of the digits in the number 100!
'''
from math import factorial

print(sum(map(int, str(factorial(100)))))
