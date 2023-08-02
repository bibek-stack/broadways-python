# string are immutable and sequence data-type in python
# creating an empty string

a=""#empty string
b=''#empty string
c=""""""#empty string
d=str()#empty string

#creating a non-empty string
a="hello world"
b= 'python is a high level language'
c=""""

Hello World.
python is awesom
"""
#quote characters
a="i'm learning python"
b= 'he said, "python is easy to learn"'

#we can also escape characters for in string with quote
a='i\'m learning python'
b="he said, \"python is easy to learn\""

#escape characters are the characters in python which suppress the actual python
#meaninf and gives new meaning to that character.
#\',\",\n, \t etc are the examples of escape characters

print("Hello\nWorld")#print hellow in first line and world in second line
print ("Hello\tWorld")#print hellow, a tab, and world

#python also has triple quoted strings
messages ="""
I'm learning
"""""
message = '''
I'm learning python
'''
#there is no need for \' (escape sequence) for triple quotedstrings
#triple quoted strings are not only used as normal strings, but are also used to
#add  code description in functions, clases and as multiline

def addituion(a, b):
    """
    :param a: any integer value
    :param b: any integer value
    :return: sum of a and b
    """
    return a+b

help(addition)