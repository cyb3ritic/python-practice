'''     CLASSWORK 
Wrire a python program to calculate difference of two set
A = {1,12,2,6,7,8} B = {15,0,1,3,6}

'''

#python code for classwork

A = {1,12,2,6,7,8}
B = {15,0,1,3,6}
C = A.difference(B)
print("Difference between set A and B is: ", C)


#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  

Write a python program to calculate symmetric difference of two set:
A = {12,2,0,3,8} B = {15,10,12,3,6}

'''

#Python code for assignment

A = {12,2,0,3,8}
B = {15,10,12,3,6}
A_diff_B = A.difference(B)
B_diff_A = B.difference(A)
C = A_diff_B.union(B_diff_A)
print("The symmetric difference of set A and B is: ",C)