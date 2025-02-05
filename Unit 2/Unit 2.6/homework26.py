'''
Homework3
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

#Basic Budget Calculator
def budget():
    # Asks the user to input their expenses for each category
    housing = float(input("Enter your housing expenses: "))
    utilities = float(input("Enter your utilities expenses: "))
    groceries = float(input("Enter your groceries expenses: "))
    transportation = float(input("Enter your transportation expenses: "))
    healthcare = float(input("Enter your healthcare expenses: "))
    personal_care = float(input("Enter your personal care expenses: "))
    clothing = float(input("Enter your clothing expenses: "))
    debt = float(input("Enter your debt expenses: "))
    
    '''
    Requests the user the input data for each category. The user is given the category to improve user experience. Values are returned to
    program as floats to allow for decimal values.
    '''
    
    # Calculates the total spending of the user by adding all the values (expenses) inputed by the user.
    total_spending = housing + utilities + groceries + transportation + healthcare + personal_care + clothing + debt
    
    # Calculates the percentage of each expense category that the user inputed.
    percent_housing = (housing / total_spending) * 100
    percent_utilities = (utilities / total_spending) * 100
    percent_groceries = (groceries / total_spending) * 100
    percent_transportation = (transportation / total_spending) * 100
    percent_healthcare = (healthcare / total_spending) * 100
    percent_personal_care = (personal_care / total_spending) * 100
    percent_clothing = (clothing / total_spending) * 100
    percent_debt =  (debt / total_spending) * 100
    
    '''
    Example Input: housing = 1000, utilities = 200, etc.
    Example Output: percent_housing would equal the housing expense divided by the total spending, then multiplied by 100.
    In this case it would be 1000 / 1200 * 100 = 83.33%. This is done for each category.    
    '''
    
    h = percent_housing
    u = percent_utilities
    g = percent_groceries
    t = percent_transportation
    h = percent_healthcare
    p = percent_personal_care
    c = percent_clothing
    d = percent_debt
    
    '''
    I decided to convert the long variable names into single letters to make the code shorter. This is done by assigning the long variable
    to a single letter. I have done this for each category to make my bottom print statements a lot shorter .
    '''
    
    # Prints the results of the calculations performed above
    print(f"Your total spending is: ${total_spending:.2f}")
    print("The percentage of each category is as follows: ")
    print(f"You pay {h:.2f}% for housing\n{u:.2f}% for utilities\n{g:.2f}% for groceries\n{t:.2f}% for transportation\n{h:.2f}% for healthcare\n{p:.2f}% for personal care\n{c:.2f}% for clothing\n{d:.2f}% for debt")
    print(f"Thank you for using the budget calculator!")
    
    '''
    The code above will print the total spending of the user, and then it will print the percentage of each category that the user spends on.
    This will print seperate lines for each category, which I believe is the most readable way to display the information. 
    '''
budget() # Calls on the function and runs the program.
