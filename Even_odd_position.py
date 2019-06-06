# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:06:30 2019

@author: satbi
"""
print("Program to manipulate elements in even and odd positions.")

def AddUp(l):
    nl=[]
    for i in range(0,len(l)):
        if i%2==0:
            N=l[i]+l[i+1]
            nl.append(N)
        else:
            N=l[i]+10
            nl.append(N)
    print("The required list is:",nl)
N=list(eval(input("Enter a list of numbers: ")))
AddUp(N)

    