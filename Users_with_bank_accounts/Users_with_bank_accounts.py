class BankAccount:
    bank_name = "First National Dojo"
    all_accounts =[]
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        # print(f"{self.name} Deposited: ${amount}, curent balance is: ${balance}.")
        print(f"deposited: ${amount}")
        return self
         
    def withdrawal(self, amount):  
        if User.can_withdrawal (self.account.balance, amount):
            print (f"Withdrawal was succesful!Original Balance was ${self.account.balance} and you took ${amount} from your account.") 
            self.account.withdrawal(amount)
            print (f"remaing account balance is now ${self.account.balance}.")
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Bank account has ${self.account.balance} in it of and an intrest rate of ${self.int_rate}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(f"balance after intrest is{self.balance}")
        else:
            print("balance is 0")


class User: 
    list_of_users=[]

    def __init__(self , name, email_address):
        User.list_of_users.append(self)
        self.name = name  
        self.email = email_address 
        self.account= BankAccount(int_rate = 0.02, balance = 0)
        # self.bank_name
    
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):  
        self.account.withdrawal(amount)  
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, current Balance is: {self.account.balance}")
        
        return self

    def transfer_money(self, other_user, amount):
        other_user.account  += amount 

######## Users ########
asta = User("Asta Staria", "asta.blackbull@clover.com")
yuno = User("Yuno Grinberryall", "yuno.goldendawn@clover.com")
yami = User("Yami Sukehiro", "yami.cpt.blackbulls@clover.com")

asta.make_deposit(1000)
yuno.make_deposit(1000)
yami.make_deposit(5000)

asta.display_user_balance()
yuno.display_user_balance()
yami.display_user_balance()