#membership operation
#membership is checkout only in dicitionary keys but not in value 

student = {"name":"Bibek","age":24,"department":"cs"}
print("name" in student) #True
print("Bibek" in student)#false


#built in functions
print(len(student))#3

result = sorted(student)
print(result)# ['age', 'department', 'name']

print(str(student))#{'name': 'Bibek', 'age': 24, 'department': 'cs'}

