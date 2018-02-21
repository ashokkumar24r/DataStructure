# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:42:53 2018

@author: ashokkumar.r
"""

def LinearSearch(myItem,myList):
    position=0
    found=False
    
    while position < len(myList) and not found:
        if myItem == myList[position]:
            found=True
        position+=1
    return found

if __name__=="__main__":
    members=["ashok","kumar","sriram","darris"]
    myItem=input("Enter the name you want to search: ")
    isitFound=LinearSearch(myItem,members)
    if isitFound:
        print ("Found it")
    else:
        print ("Nope")
        