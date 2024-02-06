'''     CLASSWORK 
Write a python program to get two numbers from the user and display maximum number.

'''

#python code for classwork

a = int(input("Enter first number:\t"))
b = int(input("Enter second number:\t"))

# print(max(a,b))

def maximum(x , y):
    if x > y:
        print(f"{x} is the maximum number.")
    elif x == y:
        print('both numbers are equal.')
    else:
        print(f'{y} is the maximum number.')

maximum(a,b)


#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT

Write a python program to get three numbers from the user and display maximum number.

'''

#Python code for assignment

a = int(input("Enter first number:\t"))
b = int(input("Enter second number:\t"))
c = int(input("Enter third number:\t"))

# print (max(a,b,c))

def maximum(x,y,z):
    if x > y and x > z:
        print(x, " is the maximum number.")
    elif y > x and y > z:
        print(y, " is the maximum number.")
    else:
        print(z, " is the maximum number.")

maximum(a,b,c)