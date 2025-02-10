'''
Homework3
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
ADD COMMENTS TO DESCRIBE PROGRAM LATER WEEK!!!! 
'''

'''
This program first checks if a number is greater than 0. If true, it will print "True", else it will print "False".
'''
def positive_or_negative(num):
    if num > 0:
        print("True")
    else:
        print("False")
    return 

'''
Checks if the number inputted is greater than 16. If so it will print "True", and if not it will print "False".
'''
def is_able_to_drive(num):
    if num >= 16:
        print("True")
    else:
        print("False")
    return

'''
Checks if the number inputted is greater than 18. If so it will print "True", and if not it will print "False".
'''
def is_able_to_vote(num):
    if num >= 18:
        print("True")
    else:
        print("False")
    return

'''
Checks if the number inputted is greater than 21. If so it will print "True", and if not it will print "False".
'''
def can_buy_alcohol(num):
    if num >= 21:
        print("True")
    else:
        print("False")  
    return 

'''
Checks to see if the number inputted is greater than 65. If so it will print "True", and if not it will print "False".
'''
def senior_discount(num):
    if num >= 65:
        print("True")
    else:
        print("False")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))