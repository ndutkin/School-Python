'''
Homework7
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
for loop using num instead of i. Loop starts at 1, and constantly adds 1 to num. First checks if number is divisible by three and 5. If the number is divisible by both, "FizzBuzz" will be printed to console. If not, if will check if the number is just divisible by 3
for which it will print "Fizz" if true. If not, it will also check if the number is just divisible by 5, for which it will print "Buzz" if true. If all these fail, the program will just print the number to the console.
'''
def fizzbuzz(num):
    for num in range(1, num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    return 

'''
Checks to see if gpa value is greater than or equal to 3.5 and then checks if credits are greater than or equal to 60. If both are greater than or equal, the program prints true. If either value is false, the program will fail.
'''
def scholarship_eligibility(gpa,credits):
    if gpa >= 3.5 and credits >= 60:
        print("True")
    else:
        print("False")
    return

'''
Checks to see if num1 is greater than num2 and num3. If true, num1 is printed to console. If false, num2 will be checked against the other two numbers. If greater than both, num2 will be printed to the console. If this fails, num3 will be printed as both values
are smaller than num3.
'''
def max_of_three_numbers(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))  