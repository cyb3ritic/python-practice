'''     CLASSWORK 

write a python program to get number from the user and display table for that number.

'''

#python code for classwork

def multiplication_table(n):
    for i in range(1,11):
        print(f'{n} X {i} = {n*i}')


n = int(input("Enter a number: \t"))
multiplication_table(n)


#------------------------------------------------------------------------------------------------------#
