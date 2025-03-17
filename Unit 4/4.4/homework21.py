'''
Homework21
Name:Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Uses an if statement to check if the word is equal to the word reversed (denoted by [::-1]). Statement returns True or False depending on if the statement is a Palindrome (reads the same forwards and backwards)
'''
def is_palindrome(string):
    palindrome_string = string.lower()
    if palindrome_string == palindrome_string[::-1]:
        return True
    else:
        return False
    pass

'''
Creates two dictionaries called ana1 and ana2. Uses two for loops to check each character in a string. The for loop will then add the character, and create a count for how many of that character there is. Checks both dictionaries against eachother to make sure they have equal amount of letters. Returns True or False depending on if 
the strings have equal amount of letters.
'''    
def is_anagram(string1,string2):
    ana1 = {}
    ana2 = {}
    for char in string1.lower():
        if char in ana1:
            ana1[char] += 1
        else:
            ana1[char] = 1
    for char in string2.lower():
        if char in ana2:
            ana2[char] += 1
        else:
            ana2[char] = 1
    if ana1 == ana2:
        return True
    else:
        return False
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))