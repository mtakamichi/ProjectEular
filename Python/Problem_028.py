#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 28
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
# 500 = (1001-1)/2
print(1 + sum([16*x**2 + 4*x + 4 for x in range(1, 500+1)]))
