"""
Q17
Class CreditCard :
 Fields:  balance limit  customer account  bank
Behaviors: make payment(amount) get customer( ) get bank( ) get account( ), get balance( ) get limit( ) charge(price)

Implement Class for CreditCard and document it


Create class PredatoryCreditCard
fields: apr (annual percentage rate)
behavoours : charge(price)
"""


"""
Here Class Credit Card id defined, where customer's bank balance, balance_limit, customer_account, bank,
amount and charge price in defined.
def make_payment returns the total amount customers need to pay and charge method returns the total charge
"""
class CreditCard:
    #define the baseclass CreditCard
    def __init__(self, balance, limit, customer_account, bank, amount, price):
        #function to define default parameter
        self.balance = balance
        self.limit = limit
        self.customer_account = customer_account
        self.bank = bank
        self.amount = amount
        self.price = price

    def make_payment(self, amount):
        #function that defines, how much amount to paid
        print(f"You need to pay {self.amount}")

    def charge(self,price):
        #charge need to pay in every transaction
        return self.price

class PredatoryCreditCard(CreditCard):
    #this class in inherited from base class CreditCard
    def apr(self, annual_per_rate):
        #new addition charge need to pay
        return annual_per_rate/100

    def total(self):
        #amoung along with charge and price
        self.price = self.price + self.apr(5)
        self.amount = self.amount + self.price
        return self.amount


p = PredatoryCreditCard(1000, 500,112345,"ABC", 200,5)
print(p.total())

