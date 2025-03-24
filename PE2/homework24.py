'''
Homework24
Name:Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Uses the symbol list, length check, and for loop to check if a password is valid. The function sets global variables to False and checks if the password has an uppercase, lowercase, number, and symbol. If the password has all of these, the function will return True.
'''
def is_valid_password(word):
    symb_lst = "!@#$%&*"
    if len(word) < 8 or len(word) > 20:
            return False
    upper = lower = number = symbol = False
        
    for char in word:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            number = True
        elif char in symb_lst:
            symbol = True
    return upper and lower and number and symbol


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest24.py'))