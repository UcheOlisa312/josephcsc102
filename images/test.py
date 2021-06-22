class Onlinestore:
    def __init__(self,numberOfitemsbought,totalcost):
        self.numberOfitemsbought = numberOfitemsbought
        self.totalcost = totalcost

    def calculator(self):
        self.finalamount =self.numberOfitemsbought * self.totalcost
        self.discount =  self.finalamount  * 10/100
        if self.totalcost > 100000:
            print(f"Total cost for" +{self.numberOfitemsbought}+ "items is N"+{self.finalamount}+", with a discount of 10%, you would pay N"+{self.discount }+".You have a gift")
        else:
            print(f"Total cost of" {self.numberOfitemsbought} "items is"  { self.finalamount})

customer = Onlinestore(20,10000)
print(customer.calculator())
