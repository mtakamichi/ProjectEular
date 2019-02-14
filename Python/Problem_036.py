#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 36
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
'''
def is_palindrome(n):
    return int(n) == int(''.join(reversed(list(str(n)))))

print(sum(filter(lambda x: all([is_palindrome(x), is_palindrome(format(x, 'b'))]), range(1, 1_000_000, 2))))
