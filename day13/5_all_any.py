#all() built in function
# all function take an iterable as a parameter
#if all the elements of that iterable are truthly then it returns true

result = all([1, 2, "jon"])
print(result)# true

result = all([0, "jane"])
print(result)#false



#any (iterable) builting function
# all() function take an iterable as a parameter
#if any one of the elements of that iterable are truthly then it returns true
print(any(["",{},1]))#true
print(any([0,[[]]]))#false


#there is one exception in all()
result = all([])
print(result)#true