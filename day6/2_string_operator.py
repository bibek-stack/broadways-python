#we can concatentate strings
m1 = "Hello"
m2 = "World"
message = m1+m2
print(message) #Helloworld


# repetition operation


messge = "HelloWorld"
print(message * 3) #"HelloWorldHelloWorldHelloWorld"


#membership operation
message = "Hello World"
print("H" in message)#true
print("W" not in message)#false
print("k" in message)#false


######### built-in function that can be used in string ##############

message ="Hello World"
print(len(message)) #11
print(bool(message))#true
print(type(message))#<class 'str>

x = slice(2,6)
print(message[x])#"llo"