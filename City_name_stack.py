# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:21:46 2019

@author: satbi
"""
top=None
def check(l):
    if len(l)!=0:
        return True
    else:
        return False
def push(l,item):
    global top
    l.append(item)
    top=len(l)
def pop(l):
    global top
    if check(l):
        l.pop()
        top-=1
    else:
        print("Underflow error.")
def display(l):
    print(l[len(l)-1],"<==top")
    for i in range(0,len(l)-1):
        print(l[i])
l=[]
while True:
    ch=int(input("Enter 1 to push:\nEnter 2 to pop:\nEnter 3 to display:\n"))
    if ch==1:
        item=input("Enter name of city: ")
        push(l,item)
    elif ch==2:
        pop(l)
    elif ch==3:
        display(l)
    
    ch2=input("Enter y to continue: ")
    if ch2=='y':
        continue
    else:
        break
    

        
        
        
    