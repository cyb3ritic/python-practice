'''     CLASSWORK and ASSIGNMENT
write a python program to store name, address, contact in dictionary, and then update contact number.
'''

#python code for classwork

data = {}
name = input("Enter name:\t")
address = input("Enter your address:\t")
contact = input("Enter you contact number:\t")
data["name"],data["address"],data["contact"] = name,address,contact
print(data)

new_contact = input("Enter new contact:\t")
data.update({"contact":new_contact})

# data["contact"]=new_contact
print(data)


