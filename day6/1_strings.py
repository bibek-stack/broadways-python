###### accessing characters in string #######
# we access characters from string using indexing. indexing in string is similar to that of list
# forward indexing starts from 0 and reverse indexing starts from-1

message = "Hello World"
print(message[0]) #H
print(message[3]) #l
print(message[5]) #<space>

print(message[-1]) #d
print(message[-3]) #r

# if we try to access not presents in the string then it raises error
#print(message[15]) #it raises index error
#print(message[-13]) #it raises index error




############## String Slicing ################

#string slicing is also similar tio list slicing
message ="Hello World"
print(message[0:3]) #Hel
print(message[:3]) #Hel
print(message[4:]) #o World