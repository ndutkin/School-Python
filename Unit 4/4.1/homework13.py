'''
Homework13
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Calculates interest by multiplying the princpal, rate, and time together. The total is then printed to the console.
'''
def calculate_interest(principal, rate, time):
    total = (principal * rate * time)
    print(f"{total:.0f}")
    return

'''
Calculates compound interest by multiplying the principal by the rate divided by n, then raised to the power of n mutiplying my time. The amount interest is then calculated by subtracting the principal from the total value we calculated. The amount of interest is then printed to the console.
'''
def compound_interest(principal, rate, n, time):
    total = principal * (1 + rate / n) ** (n * time)
    amount_interest = total - principal
    print(f"{amount_interest:.2f}")
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest13.py'))