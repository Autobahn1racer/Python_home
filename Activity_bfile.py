# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:55:58 2019

@author: satbi
"""

import pickle

def writebinaryfile(f):

    ch='y'

    print("Writing on this file.")

    while ch=='Y' or ch=='y':
        s=[]
        act=input("Enter the activity: ")
        cat=input("Enter the category: ")
        no=int(input("Enter the participants: "))

        s.append(act)
        s.append(cat)
        s.append(no)

        pickle.dump(s,f)

        ch=input("Enter y to continue n to stop: ")

    f.close()

f=open("bfile.dat",'wb+')
writebinaryfile(f)

        
