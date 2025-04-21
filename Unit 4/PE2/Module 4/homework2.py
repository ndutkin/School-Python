'''
Homework2
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Creates Employee class.
'''
class Employee:
    def __init__ (self, name, number):
        self.name = name
        self.number = number
        pass
    
    '''
    Creates a reprintable representation of the class, typically used in debugging.
    '''
    def __repr__ (self):
        return f"Employee(name='{self.name}', number='{self.number}')"
    '''
    Creates a string representation of the class.
    '''
    def __str__ (self):
        return f"Name: {self.name}\nNumber: {self.number}"
    '''
    Getter for name and number
    '''
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
'''
Creates ProductionWorker class that inherits from Employee class.
'''   
class ProductionWorker(Employee):
    def __init__ (self, name, number, shift, pay_rate):
            super().__init__ (name, number)
            
            self.shift = shift
            self.pay_rate = pay_rate
            pass
    '''
    Creates a reprintable representation of the class, typically used in debugging.
    '''        
    def __repr__(self):
        return f"ProductionWorker(name='{self.name}', number='{self.number}', shift='{self.shift}', pay_rate={self.pay_rate})"
    '''
    Creates a string representation of the class.
    '''        
    def __str__(self):
        return f"Name: {self.name}\nNumber: {self.number}\nShift: {self.shift}\nPay Rate: {self.pay_rate}"
    '''
    Getter for shift, shift_label, and pay_rate
    '''       
    def get_shift(self):
        return self.shift
    def get_shift_label(self):
        return "Day" if self.shift == 1 else "Night"
    def get_pay_rate(self):
        return self.pay_rate
'''
Prompts user for input. Output is printed to console. 
'''
print("Enter the following details of the Employee")
print("-------------------------------------------")

name = input("Enter Employee Name:")
number =input("Enter Employee Number:")
shift = input("Enter Shift (1 for Day, 2 for Night):")
pay_rate = input("Enter Pay Rate:")
employee = ProductionWorker(name, number, shift, pay_rate)

print("-------------------------------------------")
print("Details of Employee: ")
print("-------------------------------------------")
print(employee)