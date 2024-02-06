'''     CLASSWORK 
write a python program to get 5 color name from the user in list, display that list, remove last color and then display all the colors to user.
'''

#python code for classwork
colors = []
for i in range(5):
    colors.append(input(f'enter color {i+1}: '))
print(colors)
# del colors[-1]
colors.pop()
print(colors)




#------------------------------------------------------------------------------------------------------#

'''     ASSIGNMENT  
write a python program to get 5 color name from the user in list, display that list, remove last color and then display all the colors to user.
'''

#Python code for assignment
colors = []
for i in range(5):
    colors.append(input(f'enter color {i+1}: '))
print(colors)
del colors[0]

print(colors)