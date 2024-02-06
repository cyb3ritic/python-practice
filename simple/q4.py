''' CLASSWORK    
write a python program to take age from users to check whether user able to parcipate in voting or not. If age is less than 18 then it don't allow to participate and show after how much year a person will be able to participate:
Expected result if user input 10 year then:

Sorry! You cannot participate in voting, you will be able to participate after 8 year
'''

#Python code for classwork

age = int(input("Enter your age: \t"))
if age >= 18:
    print("You can participate in voting.")
else:
    print(f'Sorry! You cannot participate in voting, you will be able to participate after {18-age} year')


#---------------------------------------------------------------------------------------------------#

''' ASSIGNMENT
write a python program to take marks from the user to check whether user able to take admission in college or not. If marks is less than 60 then it don't allow to take admission.
Expected result if user input 50 year then:

Sorry! You cannot take admission, you need 10 numbers more to take admission

'''

#Python code for assignment

name = input("Enter your name:\t")
marks = int(input("Enter marks: \t"))
if marks >= 60:
    print(f'Hello {name}! You can take admission.')
else:
    print(f'Sorry! You cannot take admission, you need {60-marks} numbers more to take admission')