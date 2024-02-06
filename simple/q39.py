'''     CLASSWORK 
write a python program to get 5 numbers in the list, pass that list in the function to multiply and add that number and display total result.
'''

#python code for classwork
a = []
for i in range(5):
        a.append(int(input(f'enter number {i+1} : ')))
def sum_of_all(a):
        return sum(a)
def product(a):
        prod = 1
        for i in a:
                prod = prod * i
        return prod

print('the sum of all numbers is: ',sum_of_all(a))
print('the product of all numbers is: ', product(a))




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to get 5 numbers in the tule, pass that tuple in the function to multiply and add that number and display total result.
'''

#Python code for assignment
a = []
for i in range(5):
        a.append(int(input(f'enter number {i+1} : ')))
a = tuple(a)
def sum_of_all(a):
        return sum(a)
def product(a):
        prod = 1
        for i in a:
                prod = prod * i
        return prod

print('the sum of all numbers is: ',sum_of_all(a))
print('the product of all numbers is: ', product(a))