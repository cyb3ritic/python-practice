'''     CLASSWORK 
write a python program to convert radian to degree.
'''

#python code for classwork
from math import radians, degrees, pi
radian = eval(input("enter the radian value: "))
# print(math.degrees(radian))
def radToDeg(rad):
    return (180/pi)*rad

print(f'corresponding degree value of {radian} radians is {radToDeg(radian)}')



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to convert degree to radian.

'''

#Python code for assignment
from math import radians, degrees, pi
degree = eval(input("enter the degree value: "))
# print(math.radians(degree))
def degToRad(deg):
    return (pi/180)*deg

print(f'corresponding radian value of {degree} degree is {degToRad(degree)}')