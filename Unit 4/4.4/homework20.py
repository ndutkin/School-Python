'''
Homework20
Name:Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Creates a blank list called ascii_convert that the ASCII characters will be assigned to. Uses a for loop to go through characters in a word. Checks if the character is ASCII and then converts the value into its equivilent ASCII value.
'''
def convert_to_ascii(string):
    ascii_convert = []
    for char in string:
        if char.isascii():
            ascii_convert.append(ord(char))
    print(ascii_convert)
    pass
'''
Uses a for loop to loop through each character in a string. If the character is ASCII, it will add it to the string_filtered string. 
'''    
def filter_non_ascii(string):
    string_filtered = ''
    for char in string:
        if char.isascii():
            string_filtered += char
    print(string_filtered)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))