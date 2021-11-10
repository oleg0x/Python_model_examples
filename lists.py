#! /usr/bin/python

x = []
print(x)
x = [1, 2, 2.718, "four", "five", ['a', 'b', 'c']]
print(x)
print("Lenght of the list:", len(x))

print()
x = ["one", "two", "three", "four", "five"]
print(x)
print(x[0], x[1])
print(x[-1], x[-2])
print(x[1:3])
print(x[-3:-1])
print(x[:2])
print(x[3:])
print(x[len(x)//2:])		# 2nd half of the list

print()
y = x						# Another ref to the same list
y[0] = 0
print(x)
print(y)

z = x[:]					# Copy of the list
z[1] = 1
print(x)
print(z)

print()
x = [1, 2, 3]
x.append(4)
print(x)

y = ['a', 'b']
x.append(y)					# Append the list as the last element
print(x)

x.insert(0, "start")
x.insert(3, 2.5)
print(x)

del x[0]
del x[5]
x.remove(2.5)
print(x)

print()
x[len(x):] = [5, 6]			# Append to the end of the list
x[:0] = [-1, 0]				# Append to the beginning of the list
print(x)
x[2:4] = []					# Delete elements from the list
print(x)

print()
x = [4, 8, 6, 0, 3, 1]
x.reverse()
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)

x = ["dd", "c", "bbbb", "aaa"]
print(x)
def cmp(str):
	return len(str)
x.sort(key=cmp, reverse=True)
print(x)

y = sorted(x)				# x is not changed, y is a copy
print(x)
print(y)

print()
b1 = "aaa" in x
b2 = "xyz" in x
print(b1, b2)

z = x + y + [1, 2]
print(z)

print()
x = [None] * 4
print(x)
x = [1, 2] * 5
print(x)

print()
x = [3, -2, 0, 11, 7, 3, 0, 3, 1, 3]
print(x)
print(min(x), max(x))
print(x.index(11))
print(x.count(3), x.count(1000))
print(sum(x))

original = [[0], 1]
shallow = original[:]
import copy
deep = copy.deepcopy(original)

shallow[0][0] = "zero"		# Modify both lists
print(original)
print(shallow)

deep[0][0] = "ZERO"			# Modify the copy only
print(original)
print(deep)
