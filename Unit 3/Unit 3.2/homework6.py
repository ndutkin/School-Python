'''
Homework6
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

def div_by_seven(num):
    for i in range(1, num):
        if i % 7 == 0:
            print(i)
    return 
'''
A function that takes in a number and prints out all the numbers that are divisible by 7 up to that number. It does this by constantly adding 1 to i and then checking if i is divisible by 7.
If it is, it prints i.
'''

def squares_of_numbers(num):
    for i in range(1, num + 1):
            if i == num:
                break
            else:
                print(i ** 2)
    return 
'''
A function that takes a number and prints out the square of all numbers up to that number.  It does this by constantly adding 1 to i and then squaring i. The program will end once i is equal to num.
'''
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest6.py')) 