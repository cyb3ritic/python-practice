'''     CLASSWORK 

write a python program to calculate union of two set
-> A = {3,2,4,5,6,7,8} B = {4,12,5,1,6,8}

'''

#python code for classwork

A = {3,2,4,5,6,7,8}
B = {4,12,5,1,6,8}
C = A.union(B)      #calling union() method
print("Union of set A and B is: ", C)

#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a Python program to calculate union of Three set:
A = {5,12,52,0,8} B = {2,5,1,9,8} C = {4,5,6,0,10}

'''

#Python code for assignment

A = {5,12,52,0,8}
B = {2,5,1,9,8}
C = {4,5,6,0,10}
D = A.union(B,C)
print("Union of set A, B and C is: ", D)