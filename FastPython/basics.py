#DataTypes
#int
a = 123
b = -321
c = 22

print(a)
print(a + b, end="|\n")
print(b * 3)

#float
a = 123.0
b = -321.43
c = 22.42

print(a)
print(a + b, end="|\n")
print(b * 3)

#string
a = "123"
b = 'example'
c = "OtherExample"

#bool
a = True
b = False

#varibles
"""
	Not much to talk about, just use snake_case please
	(since the name of the language is python, duh)
"""

print(a)
print(a + b, end="|\n")
print(b * 3)

#get user input
value = input("(Try a number) minishell → ")
if (value.isdigit()):
	print(int(value) + 5)
	print("Congratulations!")
else:
	print("Common try a number mf")

# we also have methos in python / object oriented language
if (value.isalnum()):
	print("Upercase: " + value.upper())
	print("Lowercase: " + value.lower())
else:
	print("Try a word, dude")

"""
We have the core conditional operators such as:
>
<
>=
<=
==
!=
Like any other language no much secret here.
"""
