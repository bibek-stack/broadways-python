#*args and **kwargs are the arbitrary arguments
# these arguments can take dynamic number of parameters
# they are like an expandable bucket

def addition(*args):
    print(args)#(1, 2, 3)
    print(type(args)) #tuple
    total = sum(args)
    print("Sum:", total)

addition(1,2,3)



def addition(**kwargs):
    print(kwargs)
    print(type(kwargs))
    total = sum(kwargs.values())
    print("Sum:", total)
    addition(a=1, b=2, c=3)



    
