'''     CLASSWORK 
Write a python program to get large number as starting and lower number as ending number, display that number from large to lower.
i.e. displaying numbers in reverse order
'''

#python code for classwork

start = int(input("enter starting number:\t"))
end = int(input("enter ending number:\t"))
if end > start:
    start,end = end, start
for i in range(start, end-1, -1):
    print(i, end=" ")




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to get large number as starting and lower number as ending number, display that number from large and find their sum.

'''

#Python code for assignment

start = int(input("enter starting number:\t"))
end = int(input("enter ending number:\t"))
sum = 0
if end > start:
    start,end = end, start
for i in range(start, end-1, -1):
    print(i, end=" ")
    sum += i
 
print("\n\nThe sum of numbers is :\t", sum)   