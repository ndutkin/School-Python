'''
Homework17
Name:
github link:
'''


def frequency_counter(lst):
    # your code here
    '''
    Creates a frequency dictionary by iterating through all inputs in a list. If the input is already been counted, it will increment the value by 1. If the value hasn't been counted, it will be added to the dictionary with a value of 1.
    '''
    frequency = {}
    for i in lst:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency
'''
Uses a tuple to translate letters into the NATO phonetic alphabet. Iterates through each letter in the input and then prints each corresponding NATO word.
'''
def translation(english_words):
    # your code here
    nato_words = { 'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliette',
                  'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra',
                  'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-Ray', 'Y': 'Yankee', 'Z': 'Zulu'}
    for letter in english_words:
        print(nato_words[letter])
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest17.py'))