# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:25:01 2021

@author: JOJO
"""

class XBank:
    loggedinCounter = 0
    def __init__(self,theatmpin,theaccountbalance,thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename
        XBank.loggedinCounter  = XBank.loggedinCounter + 1
    
    def CollectMoney(self, amounttowithdraw):
        if(amounttowithdraw > self.accountbalance):
            print("Sorry we are not able to process at this time")
        else:
            print("Collect your cash....Thanks for banking with Xbank")+
    
    def ChangePin(self, newPin):   
        self.atmpin = newPin
        print("Your Pin has been changed...Thanks for banking with Xbank")
    @classmethod  
    def NoOfCustomersLoggedin (cls):
        print("we have a total of" + str(cls.loggedinCounter) + " that have logged in")
        
        

f = open("C:\\Users\\JOJO\\Documents\\josephcsc102\\database.txt",'r')

#print(f.readline())
password = []
accountB = []
name = []
breaker =  []
for x in f:
   breaker = x.split(' ')
   password.append(breaker[0])
   accountB.append(breaker[1]) 
   name.append(breaker[2])
   break
    

print("enter your pin........")

pasw = input()

if(pasw ==password[0]):
    customer = XBank(password[0],accountB[0],name[0])
    print(customer)
else:
    print("sorry your password does not match")

