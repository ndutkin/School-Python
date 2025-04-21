'''
Homework2 - Personal Diary
Name: Nathaniel Dutkin
github link: github.com/ndutkin/school-python
'''
'''
Defines main function which prompts user for date, time and entry.
'''
def main():
    date = input("Enter the date of your diary entry: ")
    time =  input("Enter the time of your diary entry: ")
    entry = input("Enter your diary entry: ")
    '''
    Opens the file and appends the date, time, and entry to file.
    '''
    diary_file = open("diary.txt", "a")
    diary_file.write(f"{date}\n{time}\n{entry}\n\n")
    diary_file.close()
    '''
    Opens files in read mode, prints entries into console.
    '''
    diary_file = open("diary.txt","r")
    print("Your diary entries:")
    print(diary_file.read())
    diary_file.close()
    
'''
Calls main function to run script.
'''
main()