'''     CLASSWORK 
write a program to get 6 numbers in the list and sum that number.
'''

#python code for classwork

a=[]
for i in range(6):
    a.append(int(input(f"a[{i}] =\t")))
else:
    print(f'the sum of elements is:\t{sum(a)}')
    



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a program to get 6 numbers in the tuple and sum that number

'''

#Python code for assignment

a=[]
for i in range(6):
    a.append(int(input(f"a[{i}] =\t")))
else:
    a = tuple(a)
    print(a,f'sum of all elements in given tuple is:\t{sum(a)}', sep="\n")