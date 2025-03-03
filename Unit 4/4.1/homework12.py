'''
Homework12
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Calculates the area of a rectangle by multiplying two given sides together. The area is then printed to console.
'''
def rectangle(side1, side2):
    area = side1 * side2
    print(f"'The area of the rectangle is {area} square units'")
    return

'''
Calculates the area of a circle by multiplying a predifend value of pi by the radius squared. The area is then printed to console.
'''   
def circle(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(f"'The area of a circle is {area} square units'")
    return


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest12.py'))