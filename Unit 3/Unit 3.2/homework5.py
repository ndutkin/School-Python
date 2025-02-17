'''
Homework5
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
    I used an f-string that prints num to 1 decimal point because the doctest requires the value inputted to be printed.
    This while loop first checks if num is equal to 1. If the value isn't equal to 1, it will divide it by 2 and check the remainder to make sure it equals zero. If it equals zero it must mean the value is even, so it will be dividing by 2.
    If the num value returns a remainder it will multiply num by 3 and then add 1.
'''
def collatz_conjecture(num):
    print(f'{num:.1f}')
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else: 
            num = 3 * num + 1
        print(f'{num:.1f}')
    return 
'''
    Defining variables before the while loop. I used total_sum and number_added to make it easier to read.
    While loop that checks if number_added is less than the num input. If the number_added value is less than num, it will first add the number_added value to total_sum value, and then add 1 to number_added. Once number_added is equal to num, the total_sum will be printed to the console.
'''
def add_numbers(num):
    total_sum = 0
    number_added = 0

    while number_added < num:
        total_sum += number_added
        number_added += 1
    print(total_sum)
    return
    
if __name__ == "__main__":
    collatz_conjecture(18.0)
    import doctest
    print(doctest.testfile('doctest5.py'))