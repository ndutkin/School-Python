'''
Homework10
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
The first part creates a set of numbers from 0 to the max of the list. It is then subtracted against the actual
list that we are given. We can then print the missing number data set that we have created.
'''
def find_missing_number(lst):
    # your code here
    missing_number = sorted(set(range(0, max(lst) + 1))- set(lst))
    print(missing_number)
    return 

'''
Created a blank list named even_numbers. I then created a for loop that goes over every number given in a list and
checks if it is divisible by 2 with no remainder. If so, it will be appended to our even_numbers list. Once the loop is
over, the output will be printed to console.
'''
def even_partition(lst):
    # your code here
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest10.py'))