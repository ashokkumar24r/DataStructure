# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:04:40 2018

@author: ashokkumar.r
"""

def Sorting(InValue):
    for i in range(len(InValue)-1,0,-1):
        for j in range(i):
            if InValue[j] > InValue[j+1]:
                InValue[j],temp=InValue[j+1],InValue[j]
                InValue[j+1]=temp
    return InValue 
    
def Inserting(InValue,Item):
    
   # for i in InValue:
    #    if Item < 
    InsertList=InValue+[Item]
    return Sorting(InsertList)

def InSerting(InValue,Item):
    greater=[]
    shorter=[]
    for i in range(len(InValue)):
        if Item > InValue[i]:
            greater+=[InValue[i]]
        else:
            shorter+=[InValue[i]]
    return Sorting(greater+[Item]+shorter)
            