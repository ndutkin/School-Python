'''
Homework3
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

'''
Custom exception class for non-numeric inputs. 
'''
class NotNumericError(Exception):
    
    def __init__ (self, message):
        self.message = message  
    
    '''
    String representation of the exception class
    '''
    def __str__ (self):
        return f"NotNumericError: {self.message}"
    '''
    For debugging purposes, creates a reprintable form of the class.
    '''
    def __repr__ (self):
        return f"NotNumericError(message= '{self.message}')"
'''
Main function that prompts user for input and handles exceptions. Tries to convert input to a float and raises NotNumericError if input is not numeric.
'''    
def main():
    while True:
        try:
            num1 = input("Enter a number: ")
            if not num1.isnumeric():
                raise NotNumericError("Input is not a number.")
            try:
                num2 = float(num1)
            except ValueError:
                raise NotNumericError("Input is not a valid number.")
        except NotNumericError as e:
            print(f"Error: {e}")
            break
        else:
            print(f"Number entered: {num2}")
            
        finally:
            print("The loop has finished.")
                
'''
Runs main script to prompt user for input
'''
main() 
                
   