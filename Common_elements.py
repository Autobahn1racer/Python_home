# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:40:16 2019

@author: satbi
"""

l1=list(eval(input("Enter a list of numbers: ")))
l2=list(eval(input("Enter another list of numbers: ")))
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print("List with common elements from both lists is: ",l3)
        