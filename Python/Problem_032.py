#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 32
Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.
e.g. 39 × 186 = 7254
'''
import itertools

def tuple_to_jointed_int(tp):
    return int(''.join(map(str,tp)))

def product_of_multi_pandigit(pan, div):
    multiplicand = tuple_to_jointed_int(pan[0: div])
    multiplier = tuple_to_jointed_int(pan[div: 5])
    product = tuple_to_jointed_int(pan[5: 9])
    if multiplicand * multiplier == product:
        return product
    return 0

# [Note] The products must be 4-digits. If we assume that
# multiplicand < multiplier, their possible digits are (1,4) or (2,3).
print(sum(set(
    [product_of_multi_pandigit(pan, div) 
    for pan in itertools.permutations(range(1, 10)) 
    for div in range(1, 3)])))
