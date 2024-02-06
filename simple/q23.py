'''     CLASSWORK 
Write a python program to get name of week and show "Holiday" if user input Sunday
'''

#python code for classwork
day = input("enter name of week:\t")
if(day.upper() == 'SUNDAY'):
    print("Holiday")
else:
    print("Not a  Holiday")


#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to get name of week and show "Holiday" if user input Sunday or friday
'''

#Python code for assignment
day = input("enter name of week:\t")
if(day.upper() == 'SUNDAY' or day.upper == 'FRIDAY'):
    print("Holiday")
else:
    print("Not a  Holiday")