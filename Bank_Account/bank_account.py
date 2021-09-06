class BankAccount:
    bank_name = "First National Dojo"
    all_accounts =[]
    def __init__(self, int_rate, account_balance): 
        self.int_rate = int_rate
        self.account_balance = 0
        BankAccount.all_accounts.append(self)

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
         
    def make_withdrawal(self, amount):  
        if self.account_balance >= amount:
            print (f"Withdrawal was succesful!Original Balance was ${self.account_balance} and you took ${amount} from your account.") 
            self.account_balance -= amount
            print (f"remaing account balance is now ${self.account_balance}.")  # account balance will change depending on where it is placed in the code
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.account_balance -= amount
        return self

    @classmethod
    def display_account_info(cls):
        print(" Account Balance:", self.account_balance)
        return self

    def diplay_accounts():
        for i in cls.accounts:
            i.display_account_info()
    
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * 1.01
            print(f"balance after intrest is{self.account_balance}")
        else:
            print("balance is 0")


## Accounts ##

Izuku = BankAccount(1.01, 5000)

AllMight = BankAccount(1.01, 10000)

## Actions ##

Izuku.make_deposit(100).make_deposit(100).make_deposit(200).make_withdrawal(50).yield_interest()

AllMight.make_deposit(1000).make_deposit(1000).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).yield_interest()

