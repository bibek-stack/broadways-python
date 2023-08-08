#unlike list; tuple doesn't have like append(),remove(),pop(),insert() because tuple 
# is immutuable datatype
#only methods in tuple are index() and count()


a = (1,2,1,3,4,2,3,4,5)
result = a.index(2)
print(result)#1

result = a.index()