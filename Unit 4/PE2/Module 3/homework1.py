'''
Homework1
Name: Nathaniel Dutkin
github link: github.com/ndutkin/School-Python
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''
'''
Initalizes variables for the bank account class.
'''
class Bank_Account:
    def __init__(self,name,starting_amount):
        self.name = name
        self.account = starting_amount
        pass
    '''
    Creates a printable representation of the bank account class.
    '''
    def __repr__(self):
        return F"Bank_Account(name='{self.name}', Account Balance={self.account})"
    '''
    Creates a string representation of the bank account class.
    '''
    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    '''
    Checks if the amount is greater than 0 and adds it to the account.
    '''
    def deposit(self,amount):
        if amount > 0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print("Please deposit a positive number.")
        pass
    '''
    Checks if the amount is greater than 0 and if an account has enough funds to withdraw the amount. If so, withdraws the amount and subtracts it from the total.
    '''
    def withdraw(self,amount):
        if amount <= 0:
            print("Please withdraw an amount greater than zero.")
        elif amount > self.account:
            print("Insufficient funds.")
        else:
            self.account -= amount
            print(f"{amount} withdrawn. New balance: {self.account}")
        pass

    '''
    Simple function that prints the balance of the account.
    '''
    def check_balance(self):
        print(f"Balance: {self.account}")
        pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))