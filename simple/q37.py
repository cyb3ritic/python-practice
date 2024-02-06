'''     CLASSWORK 
write a python program to get a number from the user and find cube of that number.
'''

#python code for classwork
n = int(input('enter a number:\t'))
print(f"cube of {n} is {n**3}")




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a pytohon program to get 6 number from the user to find the square of first three number and find cube of next three number
'''

#Python code for assignment
n = []
for i in range(6):
    n.append(int(input(f'enter number {i+1} :\t')))
a = [[n[i]**2 for i in range(3)], [n[i]**3 for i in range(3,6)]]
print('new list after final operation is: ', a)
