# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:59:28 2019

@author: satbi
"""

import pickle
def readbinaryfile(f):

    f.seek(0)

    print("Reading from binary file: ")
    s1=[]

    try:

        while True:
            x=pickle.load(f)
            s1.append(x)
    except EOFError:
        pass
    for i in s1:
        if i[1]=="racing":
            print("activity= ",i[0])
            print("Category= ",i[1])
            print("Participants= ",i[2])
    f.close()

f=open("bfile.dat",'rb+')
readbinaryfile(f)
