'''
Homework8
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Adds numbers from a pre-defined list using the sum command. I'm glad this was as simple as typing sum(lst) and setting it equal to a variable. I chose total_sum.
'''
def sum_numbers(lst):
    total_sum = sum(lst)
    print(total_sum)
    return 

'''
Sorts the list of pre-defined intergers from least to greatest using the .sort command. Prints the last number in the list to console by specifying [-1] as the position.
'''
def largest_number(lst):
    lst.sort()
    print(lst[-1])
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))
