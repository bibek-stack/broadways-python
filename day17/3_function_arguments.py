# arguments in the functions are the elements that are sent in the function call
# parameters are the functions are the elements that are present in the function definition

# types of arguments ina function
#1. position / Required arguments
#2. Default arguments
# 3. arbitrary arguments

def addition(a,b, c=5 ):
    return a + b + c

result = addition(2,3,10)
print(result)#15


#here "a" and "b" are the position arguments and "c" is a default arguments
#position arguments must be sent during a function call i.e. they are the required arguments
#default arguments are not required ina function call.