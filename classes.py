# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:48:10 2018

@author: ashokkumar.r
"""

class employee:
    def __init__(self,name,IdNo):
        self.name=name
        self.IdNo=IdNo
    def blood_group(self,bg):
        self.bg=bg
    def contact(self,primary_no,secondary_no,emergency_no):
        self.primary_no=primary_no
        self.secondary_no=secondary_no
        self.emergency_no=emergency_no
        
    def getDetails(self):
        #Make sure blood group & contacts are given
        return """
              Name           : %s
              Empl Id        : %s
              Blood Group    : %s
              Emergency No   : %s
              
              """ %(self.name,self.IdNo,self.bg,self.emergency_no)
              

              
Name=input("Enter your name: ")
idno=str(input("Enter your company is no : "))


Employee=employee(Name,idno)

BGroup=input("Enter your Blood group like 'B+ve' or 'B-ve': ")

Employee.blood_group(BGroup)

primary_Contact=input("Enter the contact number: ")
secondary_Contact=input("Enter the secondary contact number (if any): ")

Emerg_Contact=input("Enter the contact number in case any emergency: ")

if secondary_Contact=='':
    secondary_Contact=None


Employee.contact(primary_Contact,secondary_Contact,Emerg_Contact)
print(Employee.getDetails())




