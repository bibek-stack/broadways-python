# python lists are mutable objects
# we can create a list by inclosing a sequence in big
# brackets[]

# we can also create a list using list() built-in function

a = [] # an empty list
b=list() # an empty list using list() function

a=[1,2,3] # non-empty list

# in this list, all data are of integer data-type. but list can also 
# have heterogenous type

a= [1, "hello", 2.1, {1,2,3}, {"a": 1, "b":2}]
# in this list, the data are of different types which is also supporter
# by a python list

# we can use built-in type() functional to check the type of an object
type([1,2,3]) #list
type([1,2,3]) #tuple
type(1) #int
# and so on............