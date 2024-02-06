'''     CLASSWORK 
write a ptogram to get 6 number in the list and display all number and then clear list and then display
'''

#python code for classwork

a = []
for i in range(6):
    a.append(int(input(f'a[{i}] =\t')))
else:
    print("before clearing the list:",a, sep='\n')
    a.clear()
    print("after clearing the list:",a, sep='\n')




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT
write a ptogram to get 6 number in the tuple and display all number and then clear list and then display  

'''

#Python code for assignment

a = []
for i in range(6):
    a.append(int(input(f'a[{i}] =\t')))
else:
    a = tuple(a)

print("before clearing the list:",a, sep='\n')
del a[0]
print("after clearing the list:",a, sep='\n')