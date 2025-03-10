'''
Homework1
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Imports random module
'''
import random

'''
defines check function. Uses abs() function to get absolute value of difference between guess and actual number. Uses if and else if loop to return a value to console
depending on the difference.
'''
def check(guess, actual_number):
    difference = abs(guess - actual_number)
    if difference == 0:
        return "You Got It!"
    elif difference < 5:
        return "Very Hot"
    elif difference < 15:
        return "Hot"
    elif difference < 25:
        return "Cool"
    elif difference >= 25:
        return "Cold"
    pass

'''
Defines main function. Sets guess variable to None. Uses while loop to keep guessing the number as long as guess is not equal to actual number.
Uses the check function to print results to console.
'''
def main(actual_number):
    guess = None
    
    while guess != actual_number:
        guess = random.randint(1, 100)
        print(check(guess, actual_number))
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))