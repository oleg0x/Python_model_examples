#! /usr/bin/python

# Strings are IMMUTABLE sequences of Unicode symbols

str1 = 'Allows embedded "double" quotes'
str2 = "Allows embedded 'single' quotes"
str3 = '''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Long comment
on several lines aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'''
str4 = """aaa
bbb"""
print(str2)
print(str2[0], str2[7:10])

print(len(str1))				# Length of the string
s = "123" + "abc" + "XYZ"
print(s)

s = '-' * 10
s += 10 * '='
print(s)

print()
print( "".join(["A", "B", "C", "D"]) )
sep = " | "
s = sep.join(["a", "bb", "ccc", "dddd"])
print(s)

print("Tabs\t and newlines\n in a\t string\n".split())
strs = s.split(sep, 2)			# split(sep=None, maxsplit=- 1)
print(strs)

print()
s = "\t Hello,   World!\t "
print(s.lstrip())
print(s.rstrip())
print(s.strip())
s = "www.python.org"
print(s.strip(".gowr"))			# Symbols to delete

print()
s = "aabbXXXccXXXddeeXXXff"
print(s.find("XXX"))			# find(sub[, start[, end]])
print(s.find("ZZZ"))
print(s.find("XXX", 0, 6))
print(s.rfind("XXX"))			# rfind(sub[, start[, end]])
print(s.index("XXX", 0, 10))	# Raise ValueError when the substring is not found
print(s.rindex("XXX"))
print(s.count("XXX"))
print(s.count("XXX", 4, 12))
print(s.startswith("aabb"), s.endswith("Zff"))

print()
s2 = s.replace("XXX", "YY")
print(s2)
table = s2.maketrans("abcd", "1234")
s3 = s2.translate(table)
print(s3)

s = "the quick Brown FOX jumps over the Lazy DOG"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())

print( s.isdigit(), s.isalpha(), s.islower(), s.isupper() )

word_list = list(s)
word_list.reverse()
text = "".join(word_list[5:12])
print(text)

print()
i = int("12345")					# String to int
f = float("3.14")					# String to float
print(i, f)
print(int("21", 16))				# 0x21 = 21h = 33
s = "-" + str(777) + "-"			# Int to string
l = [1, 3, 5, 7]
print("The list is " + str(l))		# List to string

print("aa", "bb", "cc", sep='|', end="")
print(" In the same line")
print("AA", "BB", "CC", sep='', end="\n\n")

s = "{0} is the {1} of the {2}".format("Ambrosia", "food", "gods")
print(s)
s = "{food} is the food of {user}".format(food="Porridge", user="men")
print(s)
s = "The first value is {0:<8.3f}, the second value is {1:>6.3f}.".format(2.7, 3.14)
print(s)

value = 42.42
message = f"The answer is {value:8.4f}"		# f-string
print(message)

#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#print(name, age)

import string

print()
print(repr(string.whitespace))
print(string.digits)
print(string.hexdigits)
