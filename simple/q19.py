'''     CLASSWORK 
Write a python program to get 3 number from user and put in the following equation:
a+b+ac/b(2a+3b)
'''

#python code for classwork

a = eval(input("Enter a:\t"))
b = eval(input("Enter b:\t"))
c = eval(input("Enter c:\t"))

expression = (a + b + c)*(a/b)*(2*a + 3*b)
print(expression)