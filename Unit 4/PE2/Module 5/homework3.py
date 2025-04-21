'''
Homework3
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
Defines main function which opens sales_total.txt and reads each line. It will convert each total that is read to a float and then add it to the total number. (Strip command is used to remove spaces and new lines from strings, essentially formatting it.) Prints total sales once all lines have been read.
'''
def main():
    total = 0
    count = 0
    try:
        with open("sales_totals.txt", "r") as file:
            for line in file:
                try:
                    total += float(line.strip())
                    count += 1
                except ValueError:
                    print("Skipping line due to ValueError:", line.strip())
    # try block requires except statement, so I used this to catch any errors if the file is not found.                
    except FileNotFoundError:
        print("File not found. Please make sure file exists and is in root directory.")
    '''
    Prints total sales, average sales, and number of entries. Shouldn't print anything to console if no entries were found (besides the error message above.)
    '''    
    if count > 0:
        average = total / count
        print(f"Total sales: {total:.2f}")
        print(f"Average sales: {average:.2f}")
        print(f"Entries: {count}")
'''
Calls main function to run script.
'''
main()