'''     CLASSWORK 
write a python program to display numbers from 1 to 30 , only odd numbers should be printed.

'''

#python code for classwork

for i in range (31):
    if i % 2 != 0:
        print(i, end=" ")
        
## Alternative

for i in range(1,31,2):
    print(i, end = " ")
        



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to display numbers from 1 to 30 , only even numbers should be printed.
'''

#Python code for assignment

for i in range (31):
    if i % 2 == 0:
        print(i, end=" ")
        
## Alternative

for i in range(2,31,2):
    print(i, end = " ")