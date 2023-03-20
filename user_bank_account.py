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
        print (f"Balance: ${self.balance}")
        return self

    def yield_interest(self):  ## this doesn't seem to be functioning??? 
        if(self.balance >= 0):
            self.balance += self.balance * self.interest_rate
        return self
        

# user1 = BankAccount(0.05, 500)
# user2 = BankAccount(0.05, 100)

# user1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
# user2.deposit(50).deposit(50).withdraw(100).withdraw(100).withdraw(100).yield_interst().display_account_info()
# print(user1)
# print(user2) # should display insufficient funds 

# print(user1,user2)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate = 0.05, balance = 0)
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self 
    
    def make_widthdrawal(self,amount): 
        self.account.withdraw(amount)
        return self
    
    def display_user_balance (self): 
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self
    
duy = User("Duy", "duy.lyford@gmail.com").make_deposit(100).make_deposit(200).make_widthdrawal(300).display_user_balance()
duy.account.yield_interest().display_account_info() #why can't you chain the yield_interest? 
#why does the account default to 395 when there is less than $0???? 

niss = User("Nissa", "ndapt@gmail.com").make_deposit(1000).make_widthdrawal(500).display_user_balance()
niss.account.yield_interest().display_account_info()

