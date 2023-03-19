class BankAccount:

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance 

    def deposit (self,amount): 
        self.balance += amount
        return self

    def withdraw (self, amount): 
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount: 
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self): 
        print (f"Balance: $ {self.balance}")
        return self

    def yield_interst(self):
        self.balance = self.balance * self.interest_rate + self.balance
        return self 


user1 = BankAccount(0.05, 500)
user2 = BankAccount(0.05, 100)

user1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interst().display_account_info()
user2.deposit(50).deposit(50).withdraw(100).withdraw(100).withdraw(100).yield_interst().display_account_info()
print(user1)
print(user2) # should display insufficient funds 

print(user1,user2)
