#tuples are immutable datatype in python. they are sequential datatype like list, string
#dicitionary and set

#creating an empty tuple 
a = tuple()#tuple() built-in function can be used t0 create a tuple
print(a)
a=()
print(a)

#creating non-empty tuples
a= (1, 2, "a","e", [1, 3]) #tuple elements are enclosed in parenthesis or small brackets
print(a)
a=tuple([1,2,3])
print(a) #(1,2,3)

# tuple packing and unpacking
a= 1
print(type(a)) # here 'a' is int type


#but if we add',' at the last it tuple packing
a=1,
print(a) #(1,)
print(type(a)) #here "a" is tuple (1,2,3)

a= 1,2,3
print(a) # this is also a tuple (1,"a",[1,2],{1,2})



# unpacking
a, b= 1,2
print(a)# 1; integer type
print(b)#2;integer type

a,b,c =2,"hello",["a","e","i"]
print(a)#2
print(b)#hello
print(c)#["a","e","i"]


#if number of elemets in LHS is not equal to RHS it raisers error in tuple unpacking
a,b =2,"hello",["a","e","i"] # too many values to unpack
a,b,c = 2,"hello" #not enough values to unpack


a=2
b=4
print(a)#4
print(b)#2


#creating a temporary variable 'temp'
c=a
a=b
b=c
print(a)#4
print(b)#2