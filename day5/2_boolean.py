# true and false are the boolean datatype, true and false are also
# keywords in python
# boolean type in python is the subclass of the integer class
# where false represents 0 and true represents 1



# relational operators yield boolean type
a =5
b =3
print(a>b)#true
print(b<a) #true
print(b=a)#false
print(a=b)#true

#logical operators yield boolean type

print(a>b and a!=b) #true
print (b>a or a!=b)#true
print(a==b or a<b)#false
print(not a)#false
print(not b)#false

c = None
print(not c)#true
print(not [])#true
print(not "")#true
print(not {})#true
print(not False)#true
print(not True)#false


# membership operatins yield boolean
print(2 in [1,2,3])
print ("a" not in ["a","e","i","o","u"])#false

# identity operation yield boolean
a=[1,2,3]
b=a
print(a is b)#true
print(id(a) == id(b)) #true
print(a is not b)#false



b=a.copy()
print(a is b) #false
print(id(a)==id(b)) #false
print(a is not b) #false





# we have aleardy mentioned, boolean is a subclass of int type
# let see some example
print(True +2) # 1+2=3
print(70 + False)#70*0=0
print(True + True)# 1+1=2
print(True + False)# 1+0 = 1
