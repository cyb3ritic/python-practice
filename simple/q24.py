'''     CLASSWORK 
Write a python program to get two number and operator from the user to perform Arithematic operation.
'''

#python code for classwork
first_num = eval(input("Enter first number:\t"))
operator = input("enter an operator (+,-,*,/,//,%,^):\t")
second_num = eval(input("enter second number:\t"))
if operator == '+':
    print(f'{first_num} + {second_num} = ', first_num + second_num)
elif operator == '-':
    print(f'{first_num} - {second_num} = ', first_num - second_num)
elif operator == '*':
    print(f'{first_num} * {second_num} = ', first_num * second_num)
elif operator == '/':
    print(f'{first_num} / {second_num} = ', first_num / second_num)
elif operator == '//':
    print(f'{first_num} // {second_num} = ', first_num // second_num)
elif operator == '%':
    print(f'{first_num} % {second_num} = ', first_num % second_num)
elif operator == '^':
    print(f'{first_num} ^ {second_num} = ', first_num ** second_num)
else:
    print("enter valid operator.")




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
Write a python program to get two number and operator from the user to perform Arithematic operation. And if user provide operator other than arithmetic then restrict user, using function.
'''

#Python code for assignment

first_num = eval(input('enter first number:\t'))
second_num = eval(input('enter second number:\t'))
operator = input('enter your operator (+,-,*,/)')
def operate(a,b,operator):
    if operator == '+':
        print(f'{first_num} + {second_num} = ', first_num + second_num)
    elif operator == '-':
        print(f'{first_num} - {second_num} = ', first_num - second_num)
    elif operator == '*':
        print(f'{first_num} * {second_num} = ', first_num * second_num)
    elif operator == '/':
        print(f'{first_num} / {second_num} = ', first_num / second_num)
    elif operator == '//':
        print(f'{first_num} // {second_num} = ', first_num // second_num)
    elif operator == '%':
        print(f'{first_num} % {second_num} = ', first_num % second_num)
    elif operator == '^':
        print(f'{first_num} ^ {second_num} = ', first_num ** second_num)
    else:
        print("enter valid operator.")
        return
    return

operate(first_num,second_num,operator)