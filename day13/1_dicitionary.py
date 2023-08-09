# dicitionary is the mutable datatype in python

#they have the elements in key-value pair format
#it is also the sequential datatype like and tuple

#creating an empty dicitionary
a = dict()#empty dicitionary
a={}#this as also and empty dicitionary


#creating a non-empty dicitionary
student =  {"name": "jon", "age":25, "department":"CS"}
print(student) #{'name': 'jon', 'age': 25, 'department': 'CS'}
student = dict(name="jon",age=25, department="CS")
print(student)


student = dict({"name":"jon","age":25, "department":"CS"})
print(student)#{'name': 'jon', 'age': 25, 'department': 'CS'}


student = dict(("name","jon"),("age",25),("department","CS"))
print(student)


#creating a list of dictionaries
student = [
    {"name": "jon", "age": 25, "department": "CS"},
    {"name": "jane", "age": 24, "department": "IT"},
    {"name": "hary", "age": 22, "department": "Physics"}
]

print(student)#{'name': 'jon', 'age': 25, 'department': 'CS'}