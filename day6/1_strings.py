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
print(message[2:5]) #llo


print(message[0:-2]) #Hello Wor
print(message[:-2]) #Hello Wor
print(message[-4:]) #orld
print(message[-6:-2])#"Wor"
print(message[-2:-6])#""


#updating and delecting string item
m= "Hello World"
# m[2]="L" #it raises error because string is immutable and item assigment is not possible
print(m)
del m[6]# this is also not possible 
#but we can entirely delete the string object


# iterationg string using for loop
messgae = "Hello World"
for i in messgae:
    print(i) #h,e,l,l,o,w,o,r,l,


for i in message[2: 7]:
    print(i)#l,l,o,w