'''     CLASSWORK 

'''

#python code for classwork





#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to get 5 numbers from user in array, find the minimum number
'''

#Python code for assignment

import array as arr
a = arr.array('i',[])
for i in range(5):
    a.append(int(input(f'a[{i}] = ')))
print(a)
min = a[0]
for j in range(1,5):
    if a[j] < min:
        min = a[j]

print(min)



