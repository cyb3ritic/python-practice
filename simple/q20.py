'''     CLASSWORK 
Write a python program to get 5 number from user in array and sum all number and display
'''

#python code for classwork
import array as arr

a = arr.array('i',[])
sum = 0
for i in range(5):
    a.append(int(input(f"a[{i}] = ")))
for j in range(5):
    sum = sum + a[j]

print(a)
print(sum)
#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to get 5 number from user in array, and find maximum number
'''

#Python code for assignment

import array as arr
a = arr.array('i',[])
for i in range(5):
    a.append(int(input(f'a[{i}] = ')))
print(a)
max = a[0]
for j in range(1,5):
    if a[j] > max:
        max = a[j]
print(max)