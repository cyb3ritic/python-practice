'''     CLASSWORK 
write a python program to find intersection of two set:
A = {5,2,4,6,7,1} B = (5,3,1)

'''

#python code for classwork

A = {5,2,4,6,7,1}
B = (5,3,1)
C = A.intersection(B)  #calling intersection() function with one paremeter
print("Intersection of set A and B is: ", C)


#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to find intersection of two set:
A = {5,2,4,6,7,1} B = (5,3,11) C = {4,5,12,2,1,0}

'''

#Python code for assignment

A = {5,2,4,6,7,1}
B = (5,3,11)
C = {4,5,12,2,1,0}
D = A. intersection(B,C)
print("Intersection of set A,B and C is: ", D)
