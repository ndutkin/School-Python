'''
Homework3
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''

#Basic Budget Calculator
def budget():
    #Asks the user to input their expenses for each category
    housing = float(input("Enter your housing expenses: "))
    utilities = float(input("Enter your utilities expenses: "))
    groceries = float(input("Enter your groceries expenses: "))
    transportation = float(input("Enter your transportation expenses: "))
    healthcare = float(input("Enter your healthcare expenses:"))
    personal_care = float(input("Enter your personal care expenses:"))
    clothing = float(input("Enter your clothing expenses: "))
    debt = float(input("Enter your debt expenses: "))
    
    #Calculates the total spending of the user by adding all the values (expenses) inputed by the user.
    total_spending = housing + utilities + groceries + transportation + healthcare + personal_care + clothing + debt
    
    #Calculates the percentage of each expense category that the user inputed.
    percent_housing = (housing / total_spending) * 100
    percent_utilities = (utilities / total_spending) * 100
    percent_groceries = (groceries / total_spending) * 100
    percent_transportation = (transportation / total_spending) * 100
    percent_healthcare = (healthcare / total_spending) * 100
    percent_personal_care = (personal_care / total_spending) * 100
    percent_clothing = (clothing / total_spending) * 100
    percent_debt =  (debt / total_spending) * 100
    
    #Prints the results of the calculations performed above
    print(f"Your total spending is: ${total_spending:.2f}")
    print("The percentage of each category is as follows: ")
    print(f"You pay {percent_housing:.2f}% for housing")
    print(f"You pay {percent_utilities:.2f}% for utilities")
    print(f"You pay {percent_groceries:.2f}% for groceries")
    print(f"You pay {percent_transportation:.2f}% for transportation")
    print(f"You pay {percent_healthcare:.2f}% for healthcare")
    print(f"You pay {percent_personal_care:.2f}% for personal care")
    print(f"You pay {percent_clothing:.2f}% for clothing")
    print(f"You pay {percent_debt:.2f}% for debt")
    # end of code. Possibly clean up code later this week.
    
if __name__ == "__main__":
    budget()