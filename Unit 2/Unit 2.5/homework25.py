'''
Homework2
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

def birthday(month,day,year):
    # your code here
    birthday_str = f"{month} {day}, {year}"
    print("'Your birthday is " + birthday_str + ".'")
    return 

def address(street,city,state,zipcode):
    #your code here
    address_str = f"{street}, {city}, {state}, {zipcode}"
    print("'Your address is " + address_str + ".'")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))