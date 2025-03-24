'''
Homework25
Name:Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Uses a try statement to print out the flower at the given index in a list. The function will print an error message if the index is out of range or if the input is not a number.
'''
def flowers(idx,list_of_flowers):
    try:
        print("You selected:",list_of_flowers[idx])
    except IndexError:
        print("Number out of range! Please choose a valid flower number.")    
    except TypeError:
        print("Invalid input! Please enter a number.")
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))