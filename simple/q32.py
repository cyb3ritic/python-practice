'''     CLASSWORK 
write a python program to get two number from the user, pass to function and find maximum
'''

#python code for classwork

def find_maximum(a,b):
    return a if a>b else b
first_num = int(input("enter first number:\t"))
second_num = int(input('enter second number:\t'))
max = find_maximum(first_num,second_num)
print("maximum number is: ", max)



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to get two number from the user, pass to function and find minimum
'''

#Python code for assignment

def find_minimum(a,b):
    return a if a<b else b
first_num = int(input("enter first number:\t"))
second_num = int(input('enter second number:\t'))
min = find_minimum(first_num,second_num)
print("maximum number is: ", min)