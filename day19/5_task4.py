# wap to delete all the occurrences of specified character in a given string
#> s = "all the occurrence of a specified character in a given string"
#> input = "a"
#> output = "|| occurrence of specified chrcter in given string"

s = "All the occurrence of a specified character in a given string"
char = input("pick a character")
result = ""
for each in s:
    if each.lower() == char.lower():
        continue
    result += each
    print(result)