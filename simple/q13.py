'''     CLASSWORK 
write a python program to get password from user and make sure that password should contain number and alphabetic.

'''

#python code for classwork

password = input("Enter password:\t")
if password.isalnum() :
    print("The password is alpha-numeric.")
else:
    print("invalid password")

# if(password.isalpha()):
#     print("alphabets are present.")
# if(password.isnumeric()):
#     print("Numbers are present.")


    
#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write Python program to get password from user and make sure that password should contain number and alphabets and password length should not be greater than or equal to 8.
'''

#Python code for assignment

password = input("Enter password:\t")
if(password.isalnum and len(password)<8):
    print("pasword is allowed.")
else:
    print("this password is not allowed.")