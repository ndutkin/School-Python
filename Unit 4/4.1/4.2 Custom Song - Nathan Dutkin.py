'''

Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Custom song function that is based off Jack and Jill nursery rhyme. The user will be prompted to enter two names, a object to climb, an object to fetch, an object that broke, a person who helps, and two items that were used to help. The function then prints the song with the user's inputs to the console.
'''
def custom_song():
    name1 = input("Enter the first person's name: ")
    name2 = input("Enter the second person's name: ")
    climbing = input("Enter what your characters went up: ")
    fetch = input("Enter what your characters fetched: ")
    broke = input("Enter what character 1 broke: ")
    medic = input("Enter who helped character 1: ")
    item1 = input("What did they use to help character 1: ")
    item2 = input("What else did they use to help character 1: ")
    print(f"{name1} and {name2} went up the {climbing},\nTo fetch a pail of {fetch};\n{name1} fell down and broke his {broke},\nAnd {name2} came tumbling after.\nUp {name1} got and, and home did trot,\nAs fast as they could caper,\nTo old {medic} who patched his {broke}\nWith {item1} and {item2}")
    return
custom_song()