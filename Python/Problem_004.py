#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Problem 4 - Project Euler
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def is_div3(p): #pを3桁の数で割ったとき，割り切れてかつ商が3桁になるようなものが1つでもあるか？
    return len(list(filter(lambda z: p/z < 1000, filter(lambda z: p%z==0, range(100,1000))))) !=0

#6桁の回文数全体の集合P3
P3=[100001*i + 10010*j + 1100*k for i in range(1,10) for j in range(10) for k in range(10)]
print(max(filter(is_div3, P3)))
