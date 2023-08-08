vowels= ("a","e","i","o","u")
print(vowels[0]) #"a"
print(vowels[10])#it raises error
print(vowels[2])#"i"

print(vowels[-1])#"u"
print(vowels[-10])#it raises error


#slicing
#tuple slicing is also similar to that of list
data = ["a","b","c","d","e","f","g","h","i","j"]

print(data[:9])#["a","b","c","d","e","f","g","h","i"]
print(data[0:9])#["a","b","c","d","e","f","g","h","i"]4

print(data[4:])#["e","f","g","h","i","j"]
print(data[4:9])#["e","f","g","h","i"]
print(data[7:3]) #()

print(data[2:9:2])#["c","e","g","i"] #here last value in slicing is stop size


print(data[-8:]) #["c","d","e","f","g","h","i","j"]
print(data[-7:-2])
print(data[:-4])