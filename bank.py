class Account():
    def __init__(self,account_name,acc_number):
        self.account_name=account_name
        self.acc_number=acc_number
        self.balance=0
        self.deposits=[]
        self.withdraws=[]
        

    def deposit(self,amount):
        if amount<=0:
           
        
            return f"you cannot withdraw"
        else:
            self.balance+=amount
            self.deposits.append(amount)

            return  self.balance   
          

    def withdraw(self,amount):
        self.transaction=100
        if amount<=0:    
            return f"withdraw should be greater than zero"
        elif amount>self.balance:
            return f"your balance {self.balance} you cant withdraw amount"
        else:
            self.balance-=amount+self.transaction
            self.withdraws.append(amount)
            return f"hello {self.account_name} you have withdraw {amount} your new balance is {self.balance}"
 ##Add a new method called deposits_statement 
 # which using a for loop prints
 #  each deposit in a new line           
    def  deposits_statement (self):
        for x in self.deposits:
            print(x,end="\n")
#Add a new method called withdrawals_statement which using
#  a for loop prints each withdrawal in a new line
    def  wwithdraws_statement (self):
        for x in self.withdraws:
            print(x,end="\n")

            #Add a method to show the current balance.
    def current_balance(self):
        return f"{self.balance}"



                      




#Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
#Modify the withdrawal method to append each successful withdrawal to self.withdrawals
