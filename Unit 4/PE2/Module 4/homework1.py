'''
Homework1
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Intializes Pet class
'''
class Pet:
    def __init__(self, kind, breed, age):
        self.kind = kind
        self.breed = breed
        self.age = age
    '''
    Creates a reprintable representation of the class, typically used in debugging.
    '''    
    def __repr__ (self):
        return f"Pet(name='{self.kind}', breed='{self.breed}', age={self.age})"
    '''
    Creates a string representation of the class.
    '''
    def __str__ (self):
        return f"Kind: {self.kind}\nBreed: {self.breed}\nAge: {self.age}"
    '''
    Getter for kind, breed, and age
    '''
    def get_kind(self):
        return self.kind
    def get_breed(self):
        return self.breed
    def get_age(self):
        return self.age
    '''
    Creates print_details method to print details of pets
    '''         
    def print_details(self):
        print(f"Kind: {self.kind}\nBreed: {self.breed}\nAge: {self.age}")
'''
Creates print_details method to print details of pets
'''    
pet1 = Pet("Dog", "Black Lab", 6)
pet2 = Pet("Cat", "Tabby", 5)
pet3 = Pet("Dog", "Rottweiler", 6)

'''
Print details from all three pets. Also uses getattr to print specific attributes of pets.
'''
pet1.print_details()
pet2.print_details()
pet3.print_details()
  
print(getattr(pet1, "kind"))
print(getattr(pet2, "breed"))
