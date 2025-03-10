'''
Homework16
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
Assigns values to sides A and B by indexing the first and second values from the tuple. Calculates the longest side of a right triangle by squaring both A and B, adding them together, and then taking the square root of the sum. Returns the result rounded to two decimal places.
'''
def pythagorean_thm(tuple):
    # your code here
    a = tuple[0]
    b = tuple[1]
    c = (a ** 2 + b ** 2) ** 0.5
    return int(c) if c.is_integer() else round(c, 2)
'''
Defines 4 variables, x1, x2, y1, and y2, by indexing the first and second values from two different tuples (acting as points). Calculates the distance between two points by squaring the difference between x and y values, adding them together, and then calculating the square root of the value. Resulting value is then rounded to two decimal places.
'''
def distance_between_points(tuple1,tuple2):
    x1 = tuple1[0]
    x2 = tuple2[0]
    y1 = tuple1[1]
    y2 = tuple2[1]
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return int(d) if d.is_integer() else round(d, 2) 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest16.py'))