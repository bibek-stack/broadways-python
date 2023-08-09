vowels = ["a","e","i","o","u"]



#accessing dicitionary is similar to that of accessing list elements 
student = {"name": "jon", "age": 25, "department": "CS"}
dept = student["department"]
print(dept) #CS

name = student["name"]
print(name)#jon

#print(student["dob"]) #this raises keyerror


#accessing values using get()method

department = student.get("department")
print(department)#cs
dob = student.get("dob")
print(dob)#none


#adding key value pair in dicitionary
vowels = ["a","e","i","o","u"]
vowels.append("U")
vowels.insert(2, "A")

student = {"name": "jon", "age": 25, "department": "CS"}
student["dob"] = "22 july"
print(student)#{'name': 'jon', 'age': 25, 'department': 'CS', 'dob': '22 july'}


student.update(roll_no=12)
print(student) #{'name': 'jon', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}

student["name"] = "Jane"
print(student) #{'name': 'Jane', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}

#removing a key value pair from a dicitionary


student = {'name': 'Jane', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}
result = student.pop("dob")
print(result) #22 july

print(student)#{'name': 'Jane', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}

#result = student.pop{"address"} #keyerror
#print(result)

result = student.popitem()
print(result) #('roll_no', 12)
print(student)#{'name': 'Bibek', 'age': 24, 'department': 'cs'}

student.clear()
print(student)#{}
