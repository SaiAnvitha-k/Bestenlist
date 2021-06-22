#bank account using inheritance
class BankAccount:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposit and Withdraw machine")

    def deposit(self):
        amount = float(input("Enter the deposit amount:$ "))
        self.balance += amount
        print("\n Amount Deposited:$ " , amount)

    def withdraw(self):
        amount = float(input("Enter the Withdraw amount:$ "))
        if self.balance>= amount:
            self.balance -= amount
            print("\n You Withdrew:$ ", amount)
        else:
            print("\n Insufficient Balance")

    def display(self):
        print("\n Net Available Balance=$ ", self.balance)

s = BankAccount()
s.deposit()
s.withdraw()
s.display()


#ecommerece concept
class Ecommerce():
    def search(self):
        print(input("Enter search: "))
    def product(self):
        print(input("Enter number of products: "))
    def order(self):
        order = input("want to place order? yes or no: ")
        if order == "yes":
            print("order placed")
        else:
            print("Continue to shopping")



class Child(Ecommerce):
    def checkout(self):
            print("checkout")

d = Child()
d.search()
d.product()
d.order()
d.checkout()
