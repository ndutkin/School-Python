'''
Homework14
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
#your global variables go here.

'''
Multiplies a given weight in pounds by 0.453592 to convert the value to KG. Value is rounded to two decimal places.
'''
def convert_to_kg(lbs):
    #your code here
    weight = lbs * 0.453592
    return round(weight, 2)
'''
Multiplies a given height in inches by 0.0254 to convert the value to meters. Value is rounded to two decimal places.
'''
def convert_to_meters(inches):
    # your code here
    height = inches * 0.0254
    return round(height, 2)
'''
Uses the two scripts above to convert a given weight and height to KG and meters. We then calculate BMI by dividing the weight by the height squared. Uses if and else if statements to check if the BMI value is within a certain range. For example, if the BMI is greater than or equal to 30, the program will print "obese" to the console.
'''
def bmi_calculation():
    while True:
        try:
            lbs = float(input("Enter a weight in pounds: "))
            if lbs <= 0: # Checking for valid weight input
                print("Please enter a weight greater than 0")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    while True:
        try:
            inches = float(input("Enter a height in inches: "))
            if inches <= 0: # Checking for valid height input
                print("Please enter a height greater than 0")
                continue
            break
        except ValueError:
            print("Please enter a valid number")  
    weight = convert_to_kg(lbs)
    height = convert_to_meters(inches)
    
    bmi = weight / (height ** 2) # Calculates BMI
    
    if bmi >= 30:
        print('"obese"')
    elif 25 <= bmi < 30:
        print('"overweight"')
    elif 18.5 <= bmi < 25:
        print('"normal weight"')
    else:
        print('"underweight"')
    return
bmi_calculation()