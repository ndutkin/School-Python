'''
Homework2
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

def inches_to_cm(inches):
    # your code here
    cm = inches * 2.54
    inches = 2
    print(f"{cm:.2f}")
    return 

def feet_to_meters(feet):
    # your code here
    meters = feet * 0.3048
    feet = 3
    print(f"{meters:.2f}")
    return 

def lbs_to_kg(lbs):
    # your code here
    kg = lbs / 2.20462
    lbs = 20
    print(f"{kg:.2f}")
    return 

def hours_to_minutes(hrs):
    # your code here
    minutes = hrs * 60
    hrs = 3.65
    print(f"{minutes:.1f}")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))