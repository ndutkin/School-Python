'''
Divisible by 7 Script up to 300
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
Same program from homework6. for loop has been adjusted to a range of 1-300 with a step of num + 1. This means that whenever a number is inputted (I used 0) the program will count 0+1... 1+1... and so on. The number will be checked with the if statement to see if it is
divisible by 7 and has a remainder of 0. If so, it will print the number.
'''
def divisible_by_seven(num):
    for i in range(0, 300, num+1):
        if i % 7 == 0:
            print(i)
    return

divisible_by_seven(0)

