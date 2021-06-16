class Orange:
    def __init__(self, thequantity, thepriceperunit):
        self.quantity = thequantity
        self.priceperunit = thepriceperunit

    def checkQuantityRequested (self, thequantity):
        if( thequantity > self.quantity ):
            return  -1
        else:
            return  thequantity

    def calculateTotalCost(self, thequantity):
        return  self.priceperunit * thequantity

    @staticmethod
    def displayTotalCost(cost):
        print('Total cost is #' + str(cost))

    @staticmethod
    def thankYouMessage():
        print('Thanks for shopping with us !')


theoranges = Orange(20,10)

print('Welcome to Owolabi Store, Please select Orange quantity!')
theorder = input()
quantitychecker = theoranges.checkQuantityRequested(int(theorder))

while(quantitychecker  == -1):
    print('Welcome to Owolabi Store, Please enter Orange quanity not more than ' + str (theoranges.quantity))
    theorder = input()
    quantitychecker = theoranges.checkQuantityRequested(int(theorder))

theTotalCost = theoranges.calculateTotalCost(quantitychecker)

Orange.displayTotalCost(theTotalCost)
Orange.thankYouMessage()
