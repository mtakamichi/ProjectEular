#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

Pl=[[a, b, c] for a in range(1,20) for b in range(1,20) for c in range(1,100) if a**2+b**2==c**2 and a<=b<c]
Fl=[a*b*c*(1000/(a+b+c))**3 for [a, b, c] in Pl if 1000%(a+b+c)==0]
print(int(Fl[0]))
