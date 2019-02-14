#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 39
Integer right triangles
'''

def perimeter_of_right_integer_triangle(b):
    pl = []
    for a in range(1, b+1):
        c = (a**2 + b**2)**0.5
        if c.is_integer():
            pl.append(int(a + b + c))
    return pl

ph = [0]*1001
for b in range(4, 501):
    pl = perimeter_of_right_integer_triangle(b)
    for p in pl:
        if p <= 1000:
            ph[p] += 1
    
print(ph.index(max(ph)))
