'''     CLASSWORK 
write a python program to generate 1 to 10 number with their squalre and also display their addition (square + cube)
'''

#python code for classwork

print('Number','Square','Cube','Addition',sep='\t')
for i in range(1,11):
    print(i,i**2,i**3,i*i*(i+1),sep='\t')



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to generate 10 to 1 numbers(Having 4 Difference) with their square and cube and also display their sum(square + cube)
'''

#Python code for assignment
print('Number','Square','Cube','Addition',sep='\t')
for i in range(10,1,-4):
    print(i,i**2,i**3,i*i*(i+1),sep='\t')