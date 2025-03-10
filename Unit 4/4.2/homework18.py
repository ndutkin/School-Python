'''
Homework18
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

def iterate_dictionary(lst):
    dict = {1:"one",2:"two",3:"three"}
    for num in lst:
        try:
            print(dict[num])
        except:
            print("Number not in dictionary")
    # your code here
    return
'''
Uses a for loop to check values in a list. If the value is greater than 0, it will be printed to console. If the value is not greater than 0, the script will print "not positive" to the console.
'''
def check_if_positive(lst):
    # your code here
        for i in lst:
            if i > 0:
                print(i)
            elif ValueError:
                print("not positive")
        return
'''
Uses a for loop to iterate through a list of numbers. This script start at 100 and divides it by each number in the list. The script will check if the number is zero, and will print "can't divide by zero". The script will continue through each value until all values have been checked.
'''
def division(lst):
    # your code here
    for i in lst:
        try:
            print(round(100 / i, 2))
        except ZeroDivisionError:
            print("can't divide by zero")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest18.py'))