'''     CLASSWORK 
write a python program to get a username from the user that should have alphanumeric characters, then pass that username to function as parameter to display that username
'''

#python code for classwork

user_name = input('enter your username:\t')
def get_user(user_name):
    print(user_name)
if user_name.isalnum():
    get_user(user_name)
else:
    print('your username must be alphanumeric')




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to get a username from the user and make sure thet username should contain alphanumeric character and username length should not be less than or equal to 8.
'''

#Python code for assignment
user_name = input('enter your username:\t')
def get_user(user):
    print(user)
if not user_name.isalnum():
    print('your username must be alpha numeric')
elif len(user_name) <= 8:
    print('your username must not be less than or equal to 8')
else:
    get_user(user_name)
