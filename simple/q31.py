'''     CLASSWORK 
write a python program to get marks of student to find its grade using following criteria:
>=95 : show A+ grade
>=80 : show A grade
>=70 : show B grade
>=60 : show C grade
Lower than 60, will be fail(consider)
'''

#python code for classwork
marks = int(input('enter your marks:\t'))
if marks >= 95:
    print('A+ grade')
elif marks >= 80:
    print('A grade')
elif marks >= 70:
    print('B grade')
elif marks >= 60:
    print('C grade')
else:
    print('fail')




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to get scale from employer and then display salary according to Employer scale using following criteria, if:
scale is 9, display 10,000
scale is 12, display 20,000
scale is 15, display 40,000
scale is 18, display 50,000
scale is 20, display 70,000
'''

#Python code for assignment
scale = int(input("enter scale:\t"))
if scale == 9:
    print('salary is 10,000')
elif scale == 12:
    print('salary is 20,000')
elif scale == 15:
    print('salary is 40,000')
elif scale == 18:
    print('salary is 50,000')
elif scale == 20:
    print('salary is 70,000')
else:
    print("enter valid scale.")
