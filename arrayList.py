# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

myList = [16, 6, 4, 12, 9, 19, 0, 10, 3, 11, 17, 8, 5, 2, 15, 7, 18, 14, 1, 13]

dummyList=[-1,-2,-3]

print("Here are my List that i created for processing")

print (myList)

print("Appending values in to the existing List")

myList.append(dummyList[0])
print ("Value for appending one = {}".format(myList))

myList.append(dummyList[1:])
print ("Value for appending one = {}".format(myList))

print("Inserting values into the list")
myList.insert(12,56)

print(myList)

print("Popping the Last value")
print(myList.pop())

print("Index of the occurance ex. '8' ")
print(myList.index(8))

print("Poping the index value")
print(myList.pop(myList.index(8)))

print("Extending list by concanating with dummy list")
myList.extend(dummyList)

print("Final Value = %s" %(myList) )

print("Sorting by reverse")
myList.reverse()
print(myList)

myList.sort()
print("Sorted = %s" %(myList))
