'''
Homework11
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Uses two for loops to check each row and check each number in the row. Program then uses an if statement to check if any num is equal to 0,
if the num is equal to zero, it will add one to the total zeros counter. The total zeros counter will be outputted once the list of numbers has
been gone through.
'''
def count_zeros(lst):
    # your code here
    total_zeros = 0
    for row in lst:
        for num in row:
            if num == 0:
                total_zeros += 1
    print(total_zeros)
    return 

'''
Uses two for loops to check each row and each number in the row. Program uses an if statement that checks if
a number is less than 0 (negative). If the number is less than 0, it will be replaced with zero. The entire list
will be printed once the list has been gone through.
'''
def replace_with_zero(lst):
    # your code here
    for row in range(len(lst)):
        for num in range(len(lst[row])):
            if lst[row][num] < 0:
                lst[row][num] = 0
    print(lst)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest11.py'))