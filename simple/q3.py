''' CLASSWORK   
write a program to get name and age from the user and display name and age on the screen in this format:
Expected result if name is "Samip Shah" and age is 25 then:

Hi Samip Shah! Your age is 25.

'''
#python code for classwork

name = input("Enter your name:\t")
age = int(input("Enter your age:\t\t"))
print("Hi",name, end="! ")
print("Your age is", age)

#-------------------------------------------------------------------------------#

''' ASSIGNMENT
write a program to get marks and addres from the user and display on the screen in this format:
Expected result:

Your address is "..." and your marks id "..."

'''

#Pyhthon code for assignment

address = input("Enter your address:\t")
marks = int(input("Enter your marks:\t"))
print(f'Your address is "{address}" and your marks is "{marks}"')