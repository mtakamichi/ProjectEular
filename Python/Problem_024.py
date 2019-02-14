#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 24
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import itertools

digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
per_digits= list(itertools.permutations(digits))
print(''.join(list(per_digits[999999])))
