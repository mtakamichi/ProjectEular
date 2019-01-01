#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 23
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
def div_sum(x):
    return sum(filter(lambda z: x%z==0, range(1,x)))

def is_abundant(x):
    return x < div_sum(x)

abundant_list = list(filter(is_abundant, range(1, 28123)))

sum_of_two_abundants = {x+y for x in abundant_list for y in abundant_list}
print(sum(set(range(1,28123))-sum_of_two_abundants))
