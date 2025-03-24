'''
Homework26
Name:Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Uses the try statement to print out the price of a flower in a dictionary. The function will print an error message if the flower is not within the dictionary.
'''
def dictionary_exceptions(key,dict):
    try:
        print("The price of",key,"is $"+str(dict[key]))
    except KeyError:
        print("Error: Flower not found! Please enter Rose, Lily, or Tulip.")  
    pass

'''
Uses the try statement to print out the character at the given index for a string. The function will print an error message if the index is not within the string.
'''
def string_exceptions(idx,str):
    try:
        print("The character at index",idx,"is:",str[idx])
    except TypeError:
        print("Error: String indices must be integers, not 'str'")
    except IndexError:
        print("Error: Index out of range! Please enter a valid index.")
    except ValueError:
        print("Error: Please enter a valid number for the index.")
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest26.py'))