'''

  Q17
Class CreditCard :
 Fields:  balance limit  customer account  bank
Behaviors: make payment(amount) get customer( ) get bank( ) get account( ), get balance( ) get limit( ) charge(price)

Implement Class for CreditCard and document it


Create class PredatoryCreditCard
fields: apr (annual percentage rate)
behavoours : charge(price)


'''

class CreditCard :
    def __init__(self, balance, limit, customer, account, bank, **kwargs):
        self.balance=balance
        self.limit=limit
        self.customer= customer
        self.account= account
        self.bank=bank
        
    def make_payment(self):
        x= int(input("Enter amount to be paid"))
        x= self.balance- x
        print("New balance =",x)
        self.balance=x

    def get_customer(self):
        print("the customer details , Name :",self.customer)

    def get_balance(self):
        print("Your Balance is :", self.balance)

    def get_limit(self):
        print("Your limit is is :", self.limit)


if __name__ == '__main__':
    v= CreditCard(50000, 1000, "Ram", "savings", "NICASIA")
    v.make_payment()
    v.get_customer()
    v.get_limit()
    v.get_balance()
