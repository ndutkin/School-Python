'''
Homework22
Name:Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
Creates a blank masked string. Saves last four digits into a value called last_four. Then uses a for loop to iterate through each letter in a string and replaces them with "*". The for loop doesn't include the last 4 digits of the string. After the string has been obfuscated, it will be returned with the last four to console.
'''
def mask_creditcard(string):
    masked_string = ''
    last_four = string[-4:]
    
    for char in range(len(string)- 4):
        if string[char].isdigit():
            masked_string += '*'
    return masked_string + last_four
    pass
'''
Uses a for loop to check each character in a string. Checks if the characters is in the Vowels string. If so, it will be removed from the string and replaced with nothing.
'''    
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            string = string.replace(char,'')
    return string
    

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest22.py'))