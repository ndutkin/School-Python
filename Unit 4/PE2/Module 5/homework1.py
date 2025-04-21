'''
Homework1
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
Creates a function that generates all two-letter combinations from a given set of letters which is defined in main. The function uses yield to return each combination one at a time. Uses two nested for loops to create the combos.
'''
def two_letter_combos(letters):
    for one in letters:
        for two in letters:
            yield  one + two
'''
Main function where letters are defined, the blank combos list is created, and two_letter_combos is called to. Prints each combo that is generated from above function.
'''
def main():
    letters = 'aenst'
    combos = [] 
    for letter in two_letter_combos(letters):
        print(letter)
'''
Calls main function to run script.
'''        
main()