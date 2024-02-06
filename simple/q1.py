'''  Classwork  
Write a program to show such type of layout of number and its square.
Expected result:

Number      Square
1           1
2           4
3           9
4           16
5           25

'''
# Writing MY Python code for classwork

print("Number","Square", sep="\t\t")
for i in range(1,6):
    print(i,i**2, sep="\t\t")

#----------------------------------------------------------------------------------------------------------#

'''  ASSIGNMENT
Write a python program to show such type of layout of number, square and cube.
Expected result:

Number      Square      Cube
1           1           1
2           4           8
3           9           27
4           16          64
5           25          125

'''

# Python code for assignment

print("Number","Square", "Cube", sep="\t\t")
for i in range (1,6):
    print(i,i**2,i**3, sep="\t\t")