'''
Homework4
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
ADD COMMENTS TO DESCRIBE PROGRAM LATER WEEK!!!! 
'''
'''
Uses multipled if and else if statements to check if the number inputted is equal to a letter grade. The first if statement checks to make sure the score is within 0-100. Then it checks if the score is between 90-100 = A, 80-89 = B, and so on.
'''
def grade_calculator(score):
    if score < 0 or score > 100:
        print("'Enter a grade between 0-100'")
    elif score >= 90:
        print("'A'")
    elif score >= 80:
        print("'B'")
    elif score >= 70:
        print("'C'")
    elif score >= 60:
        print("'D'")
    elif score < 60:
        print("'F'")
    return

'''
Checks to see if a number inputted is divisible by 2 and leaves a remainder of zero. If so, the program will print "even", and if not the program will print "odd"
'''
def even_or_odd(num):
    if num % 2 == 0:
        print("'even'")
    else:
        print("'odd'")
    # your code here
    return 



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))