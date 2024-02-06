'''     CLASSWORK 
write a python program to get starting number and ending number from the user to display that number with proper sequence.

As, user input 5 as starting number and 10 as ending number, then it should display 5 6 7 8 9 10

'''

#python code for classwork

start = int(input("enter starting number:\t"))
end = int(input("enter ending number:\t"))
for i in range(start, end+1, 1):
    print(i, end=" ")

#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to generate number from start to end number with properly 4 number difference. As 1 5 9 13 17 if start is 1 and end is 18

'''

#Python code for assignment

start = int(input("enter the staring number:\t"))
end = int(input("enter ending number:\t"))
for i in range (start, end, 4):
    print(i, end=' ')