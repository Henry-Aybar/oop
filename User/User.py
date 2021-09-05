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

    def make_withdrawal(self, amount):  
        self.account_balance -= amount  # the specific user's account decreases by the amount of the value withdrawan

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

##=================##
##    Deposits     ##
##=================##

## Guido 
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_deposit(500)

## Monty
monty.make_deposit(75)
monty.make_deposit(50)

#Izuku
izuku.make_deposit(5000)

##===================##
##    Withdrawals    ##
##===================##

## Guido 
guido.make_withdrawal(150)
guido.make_withdrawal(25)

## Monty
monty.make_withdrawal(10)
monty.make_withdrawal(5)

## Izuku
izuku.make_withdrawal(100)
izuku.make_withdrawal(20)
izuku.make_withdrawal(5)


## Call Display Method
guido.display_user_balance()
monty.display_user_balance()
izuku.display_user_balance()


##===================##
##    Transfers      ##
##===================##

guido.transfer_money(izuku, 5)

## Call Display Method
print("After Money Transfer")
guido.display_user_balance()
izuku.display_user_balance()
