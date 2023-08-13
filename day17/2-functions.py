# functions are the block of codes that are re-usable
# if the same line code are repeated at multiple places in the code, then we can define a function
# for the code block and call wherever necessary

# there are things we need to keep in mind while creating a function:
# 1. function definition
#2. function call


# lets create a simple function to check whether a number is odd ar een


def is_even(number): # This is a function definition
    if number %2 ==0:
        return True
    else:
        return False
    

    def is_even_n(number):
        return number % 2 == 0
    

result = is_even(43) #function call
print(result) #false



def addition(n1, n2): #function definition
    return n1 + n2

result = addition(4, 5)#function call
print(result)#9




