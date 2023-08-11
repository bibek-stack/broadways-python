# condition in python any programming language is used to make decisions
# we can make conditions in python in three different ways 
# 1. simple if
#2. if...else block
# 3. if ...elif leader

#note :Nested if conditions are possible 

# 1. simple if
age = 30
if age > 19:
    print("The person is not a teenger")

    # if conditions always takes truthly statement is truthly the block inside
    # if conditions is executed. if galsy the block insid if is not executed



    if age:
        print(f"The person's age is {age}")


    vowels = []
    if vowels:
        print(vowels)



a = 2
if a:
    print(f"The number is {a}")




#2. if...else block
age = 18
if age > 19:
    print("The person is not teenager")

else:
    print("The person is a teneager")


if age:
    print(f"The person's age is {age}")

else:
    print("The age is not provided")



    vowels = []
    if vowels:
        print(vowels)
    else:
        print("The list is empty")


data = [1,2,3,4,5]
if 2 in data:
    print(" 2 is present in the list")
else:
    print("2 is not list")

    num = 5
    if not num:
        print("The number is not given")
    else:
        print("The given number is {num}")


    
# 3. if ...elif leader

exam_percent = 76 in(input("Enter the exam percentage"))
if exam_percent > 80:
    print("The student got distinction")
elif exam_percent > 65:
    print("The student got first division")

elif exam_percent > 55:
    print("The student got second division")

elif exam_percent > 40:
    print("The student got third division")

else:
    print("The student failed !!")



# ternary if
a = 5
if a > 10:
    print("The number is greater than 10")
else:
    print("The number is less than 10")


# this is ternary if condition
    print("The number is greater than 10") if a > 10 else print("The number is less than 10")


# nested if = nested if is simply if condition inside a if condition
a = 20
if a > 10:
    if a > 15:
        print("The number is greater than 15")
    else: 
        print("The number is just greater than 10")
else:
    print("The number is less than 10")





# Python program to check if the input number is odd or even.


num = int(input("Enter a number: "))
if a % 2 == 0:
   print("{a} is Even")
else:
   print("{a} is Odd number")