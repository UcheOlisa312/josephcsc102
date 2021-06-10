class Online:
    cost_of_oranges= 50
    def __init__(self):
        self.total_amount_of_oranges=500

    def buy(self):
        print("The total amount of oranges we have is:" +{self.total_amount_of_oranges})
        print("the price of one orange is ${self.cost_of_oranges}")
        customers_amount = ("Enter the anount of oranges you want: " )
        if customer_amount>self.total_amount_of_oranges:
            print("the amount of oranges that you entewred is more than what we have.")
        elif customer_amount < 1:
            print("the amount of oranges you entered is not reasonable.")
        elif 500>customers_amount>1:
            choice=input("please confirm payment(yes/no): " )
            if choice == "yes":
                print("thanks for your patronage")
            elif choice == "no":
                print("Your purchase has been terminated")



