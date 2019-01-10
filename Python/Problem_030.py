#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 30
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
FP=[x**5 for x in range(0,10)]
print(sum(list(filter(lambda n: n == sum([FP[int(i)] for i in str(n)]) , range(10, 6*9**5)))))
