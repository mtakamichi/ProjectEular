#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 28
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
# 502 = (1001+1)/2+1
print(1 + sum([16*x**2 - 28*x + 16 for x in range(2, 502)]))
