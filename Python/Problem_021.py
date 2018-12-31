#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 21
Evaluate the sum of all the amicable numbers under 10000.
'''
from functools import lru_cache

@lru_cache(maxsize=10000)
def div_sum(x):
    return sum(filter(lambda z: x%z==0, range(1,x)))

def is_amicable(x):
    y = div_sum(x)
    return div_sum(y)==x and y!=x

print(sum(filter(is_amicable, range(1,10000))))
