#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 22
What is the total of all the name scores in the file?
'''
import csv

def alph_val(name):
    return sum(map(lambda x: ord(x)-64, name))

with open('names.txt', 'r') as f:
    reader = csv.reader(f)
    names = sorted(list(reader)[0])

alph_vals = list(map(alph_val, names))
name_vals = [x*y for x,y in zip(alph_vals, range(1, len(alph_vals)+1))]

print(sum(name_vals))
