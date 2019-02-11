#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 41
What is the largest n-digit pandigital prime that exists?
'''
import math
from itertools import permutations
# is_prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


pp_list = []
# Since all pandigital numbers made by n=5, 6, 8, 9 are divisible by 3, 
# we only need to find the maximum prime number from the 7-pandigital numbers.
for p in permutations(range(1, 8)):
    a = int(''.join(map(str, p)))
    if is_prime(a):
        pp_list.append(a)
print(max(pp_list))

# One-line solution
#print(max([a for a in [int(''.join(map(str, p))) for p in permutations(range(1, 8))] if is_prime(a)]))