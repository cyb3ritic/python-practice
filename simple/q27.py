'''     CLASSWORK 
Write a python program to check a year, wheter it is a leap year or not
'''

#python code for classwork
year = int(input('enter a year:\t'))
if year % 4 ==0:
    print("leap year")
else:
    print("not a leap year")



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to get 5 year from the user to store in array and display only leap year to user
'''

#Python code for assignment  
import array as arr
years = arr.array('i',[])
for i in range(5):
    years.append(int(input(f'enter year {i+1}: ')))
print(years)
leap_years = []
for j in range(5):
    if years[j] % 4 == 0:
        leap_years.append(years[j])
else:
    if len(leap_years) > 0:
        print('the leap years are: ', leap_years)
    else:
        print('there is no leap_year is this array')