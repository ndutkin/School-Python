'''
Homework2
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

def birthday(month,day,year): 
    birthday_str = f"{month} {day}, {year}"
    print("'Your birthday is " + birthday_str + ".'")
    return 
'''
Example Input: month = Feburary, day = 6, year = 2025
Example Output: 'Your birthday is Feburary 6, 2025.'
The apostrophes are included in the output as it is required for the doctest to pass. The function includes these apostrophes.
Prints out the birthday in the format of "Month Day, Year". This is done with birthday_str that converts the variables into a string.
'''

def address(street,city,state,zipcode):
    address_str = f"{street}, {city}, {state}, {zipcode}"
    print("'Your address is " + address_str + ".'") # I am then able to print the address in the format of "Street, City, State, Zipcode" in a readable format.
    return 
'''
Example Input: street = 1234 Main St, city = Crystal Lake , state = IL, zipcode = 60012
Example Output: 'Your address is 1234 Main Street, Crystal Lake, IL, 60012.'
Does something similar to the birthday function, but with an address. The address_str variable above converts the variables into a string of text
which can be inputed wherever.
'''
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))