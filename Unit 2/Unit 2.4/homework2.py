'''
Homework2
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

def inches_to_cm(inches):
    # Converts inches into centimeters. Rounds to 2 decimal places.
    cm = inches * 2.54
    inches = 2
    print(f"{cm:.2f}")
    return 

def feet_to_meters(feet):
    # Converts feet into meters. Rounds to 2 decimal places.
    meters = feet * 0.3048
    feet = 3
    print(f"{meters:.2f}")
    return 

def lbs_to_kg(lbs):
    # Converts pounds into kilograms. Rounds to 2 decimal points.
    kg = lbs / 2.20462
    lbs = 20
    print(f"{kg:.2f}")
    return 

def hours_to_minutes(hrs):
    # Converts hours into minutes. Rounds to 1 decimal point.
    minutes = hrs * 60
    hrs = 3.65
    print(f"{minutes:.1f}")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))