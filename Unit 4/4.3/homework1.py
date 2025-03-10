'''
Homework1
Name:
github link: 
'''

import random
guess = None

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
    
def main(actual_number):
    guess = None
    
    while guess != actual_number:
        guess = random.randint(1, 100)
        print(check(guess, actual_number))
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))