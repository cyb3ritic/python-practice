'''     CLASSWORK 
write a program that performs all compound assignment operations on an integer
'''

#python code for classwork

n = int(input("Enter a number:\t"))

# addition assignment operator
n += 5
print("the value of n after addition assignment operation is: \t",n)

# subtraction assignment operator
n -= 5
print("the value of n after subtraction assignment operation is:\t",n)

# multiplication assignment operator
n *= 5
print("the value of n after multiplication assignment operation is:\t",n)

# division assignment operator
n /= 5
print("the value of n after division assignment operation is: \t",n)

# modulus assignment operator
n %= 5
print("the value of n after modulus assignment operation is: \t",n)




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a program that performs all compound assignment operations on an integer. And add all the result, and then display to user
'''

#Python code for assignment

a = []
n = int(input("Enter a number:\t"))

# addition assignment operator
n += 5
a.append(n)

# subtraction assignment operator
n -= 5
a.append(n)

# multiplication assignment operator
n *= 5
a.append(n)

# division assignment operator
n /= 5
a.append(n)

# modulus assignment operator
n %= 5
a.append(n)

print(sum(a))
