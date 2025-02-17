'''
Homework9
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Simple bubble sort program that checks numbers next to eachother in a list and swaps their places if one
number is larger than the other number. For loop allows us to check all numbers given to us in a list.
'''
def bubble_sort(lst):
    # your code here
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swapped = True
                lst[i], lst[i + 1] = lst[i+1], lst[i]          
    print(lst)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest9.py'))