# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:53:05 2019

@author: satbi
"""

def Sum_rec(n):
    if n<0:
        return n+1
    else:
        return n+Sum_rec(n-1)
n=int(input("Enter a number to add till 0: "))
print(Sum_rec(n))