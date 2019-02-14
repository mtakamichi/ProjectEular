#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

from functools import reduce
from operator import mul

# Permutation of indistinguishable objects -- reduction of redundant multiplications
print(reduce(mul, range(21,41)) // reduce(mul, range(1,21)))

# Permutation of indistinguishable objects -- naive
#import math
#print(math.factorial(40)//(math.factorial(20)*math.factorial(20)))
