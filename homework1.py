'''
Homework1
Name: Nathaniel Dutkin
Github: https://github.com/ndutkin/School-Python
'''

# Literals for math operations
num1 = 15
num2 = 5
length = 228
width = 48

def add(num1,num2):
    # your code here
    add = num1 + num2
    print(add)
    return 

def subtract(num1,num2):
    # your code here
    subtract = num1 - num2
    print(subtract)
    return 

def multiply(num1,num2):
    # your code here
    multiply = num1 * num2
    print(multiply)
    return 

def division(num1,num2):
    # your code here
    division = num1 / num2
    print(division)
    return 

def int_div(num1,num2):
    # your code here
    int_div = num1 // num2
    print(int_div)
    return 

def modulus(num1,num2):
    # your code here
    modulus = num1 % num2
    print(modulus)
    return 

def exp(num1,num2):
    # your code here
    exp = num1 ** num2
    print(exp)
    return 

def area(length,width):
    # your code here
    area = length * width
    print("'The area of the rectangle with a length of " + str(length) + " and a width of " + str(width) + " is " + str(area) + "'") 
    return 


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))