# '''     CLASSWORK 
# Write a python program to check alpha character, whether vowel or consonant.
# '''

# #python code for classwork
# a = input("enter a character:\t")
# if a.upper() == 'A' or a.upper() == 'E' or a.upper() == 'I' or a.upper() == 'O' or a.upper() == 'U':
#     print("vowel")
# else:
#     print("consonant")



#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to check alpha character, whether vowel or consonant and also display "it is number", if user give any number.
'''

#Python code for assignment
a = (input("enter a thing:\t"))
if ord(a) in range(48,58):
    print("it is number")
elif a.upper() == 'A' or a.upper() == 'E' or a.upper() == 'I' or a.upper() == 'O' or a.upper() == 'U':
    print("vowel")
else:
    print("consonant")