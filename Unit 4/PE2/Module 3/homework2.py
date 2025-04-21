'''
Homework2
Name: Nathaniel Dutkin
github link: github.com/ndutkin/School-Python
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''
'''
Defines Bank_Account class with name and starting amount variables.
'''
class Bank_Account:
    def __init__(self,name,starting_amount):
        self.name=name
        self.account = starting_amount
    '''
    Creates a printable represtentation of the bank account class.
    '''
    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"
    '''
    Creates a string representation of the bank account class.
    '''
    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    '''
    Function that checks if an amount is greater than 0, if so it will add it to the account. If not, it will print a message asking for a positive deposit.
    '''
    def deposit(self,amount):
        if amount>0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print(f"Please deposit a positive number.")
    '''
    Function that checks if an amount is greater than 0 and if an account has enough funds to withdraw the amount. If so, withdraws the amount and subtracts the amount from the total.
    '''
    def withdraw(self,amount):
        if amount>0:
            if self.account-amount>=0:
                self.account-=amount
                print(f"{amount} withdrawn. New balance: {self.account}")
            else:
                print(f"Insufficient funds.")
        else:
            print(f"Please withdraw an amount greater than zero.")

    '''
    Simple function that prints the balance of the account.
    '''
    def check_balance(self):
        """
        Check and return the balance of the account holder's account.
        """
        print(f"Balance: {self.account}")
'''
Defines SavingsAccount class that inherits from Bank_Account and adds an interest rate variable.
'''
class SavingsAccount(Bank_Account):
    def __init__(self, name, starting_amount, interest_rate=1.0):
        super().__init__(name, starting_amount)
        self.interest_rate = interest_rate
    '''
    Creates a printable representation of the savings account class.
    '''
    def __repr__(self):
        return (f"SavingsAccount(account_holder='{self.name}', balance={self.account},"f" interest_rate={self.interest_rate}%)")
    '''
    Creates a string representation of the savings account class.
    '''
    def __str__(self):
        return (f"Savings Account - {self.name}: Balance = ${self.account:.2f}, Interest Rate = {self.interest_rate}%")
    '''
    Function that applies interest to the account balance based on the interest rate.
    '''
    def apply_interest(self):
        interest = self.account * (self.interest_rate / 100)
        self.account += interest
        return self.account
    pass
'''
Defines CheckingAccount class that inherits from Bank_Account and adds an overdraft limit variable.
'''
class CheckingAccount(Bank_Account):
    def __init__(self, name, starting_amount, overdraft_limit=100.0):
        super().__init__(name, starting_amount)
        self.overdraft_limit = overdraft_limit
    '''
    Creates a printable representation of the checking account class.
    '''        
    def __repr__ (self):
        return (f"CheckingAccount(account_holder='{self.name}', balance={self.account}, "f"overdraft_limit={self.overdraft_limit})")
    '''
    Creates a string representation of the checking account class.
    '''
    def __str__ (self):
        return (f"Checking Account - {self.name}: Balance = ${self.account:.2f}, Overdraft Limit = ${self.overdraft_limit:.2f}")
    '''
    Function that checks if an amount is greater than 0 and if the account has enough funds to withdraw the amount. If so, withdraws the amount and subtracts it from the total.
    '''
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.account + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.account -= amount
            return self.account
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))