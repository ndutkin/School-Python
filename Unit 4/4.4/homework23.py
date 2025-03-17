'''
Homework23
Name:Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Creates a blank dictionary to create a list of letters. Uses a for loop to iterate through each word in a list of words. Sets first_letter variable to equal word[0], meaning it will equal the first letter for whatever word in our for loop. For loop will check if a letter is in the dict, and if so it will add the word to the list.
If not, the statement will add the first letter to the dictionary.
'''
def group_by_first_letter(words):
    dict = {}
    for word in words:
        first_letter = word[0]
        if first_letter in dict:
            dict[first_letter].append(word)
        else:
            dict[first_letter] = [word]
    return dict  

'''
Uses a simple return statement to join the words given in the words list. Adds a period at the end to create a sentence.
'''
def convert_to_sentence(words):
    return  ''.join(words) + '.'

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest23.py'))