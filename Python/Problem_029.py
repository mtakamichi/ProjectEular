#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 29
How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
'''
print(len({a**b for a in range(2, 100+1) for b in range(2, 100+1)}))