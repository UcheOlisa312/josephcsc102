# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Coffee:
    coffeeCupCounter = 0 # initialize class variable
    def __init__(self,themilk, thesugar, thecoffeemate):
        self.milk = themilk # initialize instance variable
        self.sugar = thesugar #initialize instance variable
        self.coffeemate = thecoffeemate # initialize instance variable
        Coffee.coffeeCupCounter= Coffee.coffeeCupCounter +1
        print(f"you now have your coffee with{self.milk} milk, {self.sugar} sugar and {self.coffeemate} coffeemate")
        
 
mySugarFreeCoffee = Coffee(2,-200,1) # instantiation - object creation 
print(mySugarFreeCoffee.sugar)
myMuchSugarCoffee = Coffee(2,10,1)
print(myMuchSugarCoffee.sugar) # instantiation or object variable
print(f"we have made {Coffee.coffeeCupCounter} coffee cups so far!")
print(f"we have made {mySugarFreeCoffee.coffeeCupCounter} coffee cups so far")
print(f"we have made {myMuchSugarCoffee .milk} coffee cups so far!")
print(f"we have made {myMuchSugarCoffee.coffeeCupCounter} coffee cups so far!")