'''     CLASSWORK 
write a python programto get 6 subject marks from the user and calculate total average and percentage of that marks. And display to user.

'''

#python code for classwork

marks =[]
n = int(input("Enter the number of subjects:\t"))
for i in range(n):
    marks.append(int(input(f"marks in subject[{i}] = ")))


def calculate(array):
    total_marks = sum(array)
    average = total_marks/len(array)
    print(f"Total marks obtained is:\t {total_marks}")
    print(f'Average of marks is:\t\t {average}')


calculate(marks)

#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  

'''

#Python code for assignment