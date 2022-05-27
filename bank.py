class Account():
    def __init__(self,account_name,acc_number,balance,new_money):
        self.account_name=account_name
        self.acc_number=acc_number
        self.balance=balance
        self.new_money=new_money

    def deposit(self):
        self.balance+=self.new_money
        return f"hello {self.account_name} your new balance {self.balance}"    

    def withdraw(self):
        self.balance-=self.new_money
        return f"hello {self.account_name} your new balance {self.balance}"    
    
        