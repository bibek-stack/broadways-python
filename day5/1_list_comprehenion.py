# we can do loop through the list in following way

a = [1,2,3,4,5]
for i in a:
    print(i)

    b = []
    for i in a:
        value = i ** 2
        b.append(value)
        print(b)
# recreating the above code using list comprehension
        result = [i**2 for i in a]
        print(result)