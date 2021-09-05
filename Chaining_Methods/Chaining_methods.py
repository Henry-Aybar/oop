class User:     
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):
        self.name = name  
        self.email = email_address 
        self.account_balance = 0
        self.bank_name
    
     # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):  
        self.account_balance -= amount  # the specific user's account decreases by the amount of the value withdrawan
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, current Balance is: {self.account_balance} at {self.bank_name}")

    def transfer_money(self, other_user, amount):
        other_user.account_balance  += amount 

## Guido's info
guido = User("Guido van Rossum", "guido@python.com")
guido.bank_name = "Dojo Credit Union"


## Monty's info
monty = User("Monty Python", "monty@python.com")

## Izuku's info
izuku = User("Izuku Midoriya", "imidoriya@stu.ua.com" )
izuku.bank_name = "UA Bank 'Be Plus-Ultra!'"

##========================##
##        Guido's         ##
## Deposits & Withdrawals ##
##========================##

guido.make_deposit(200).make_deposit(100).make_deposit(500).make_withdrawal(150).make_withdrawal(25).display_user_balance()

##========================##
##        Monty's         ##
## Deposits & Withdrawals ##
##========================##

## Monty
monty.make_deposit(75).make_deposit(50).make_withdrawal(10).make_withdrawal(5).display_user_balance()

##========================##
##        Monty's         ##
## Deposits & Withdrawals ##
##========================##

#Izuku
izuku.make_deposit(5000).make_withdrawal(100).make_withdrawal(20).make_withdrawal(5).display_user_balance()


##===================##
##    Transfers      ##
##===================##

guido.transfer_money(izuku, 5)

## Call Display Method
print("After Money Transfer")
guido.display_user_balance()
izuku.display_user_balance()