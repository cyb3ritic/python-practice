'''     CLASSWORK 
write a pyh=thon program to get 10 Name of the students from the user in a list, display that students name in last to first order.
'''

#python code for classwork
students = []
for i in range(10):
    students.append(input(f'enter name of student{i+1}: '))
students.reverse()
print(students)



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a pyh=thon program to get 10 Name of the students from the user in a list, display that students name in last to first order with removing last and first student name
'''

#Python code for assignment
students = []
for i in range(10):
    students.append(input(f'enter name of student{i+1}: '))
students.pop()
students.reverse()
students.pop()
print(students)