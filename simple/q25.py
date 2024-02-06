'''     CLASSWORK 
Write a python program to get student marks, if marks is less than 40, display fail otherwise pass.
'''

#python code for classwork
mark = int(input('enter marks:\t'))
if mark <40:
    print("fail")
else:
    print("pass")




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to get student name, if student name is xyz, then don't allow him to take admission
'''

#Python code for assignment
name = input("enter your name:\t")
if name == 'xyz':
    print("you can't take admission.")
else:
    print("you can take admission.")