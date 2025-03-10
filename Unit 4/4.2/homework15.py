'''
Homework15
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
First checks if number is equal to 0 or 1, if so, returns 1. Otherwise, returns the number multiplied by the factorial of the number minus 1.
'''
def factorial(n):
    # your code here
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    return
'''
Creates a factorial result by calling on the factorial function. Prints the result of the factorial to console.
'''
def main(num1):
    # your code here
    factorial_result = factorial(num1)
    print(f'"The factorial of {num1} is {factorial_result}."')
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest15.py'))