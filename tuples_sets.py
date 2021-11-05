#! /usr/bin/python

'''
Tuples are immutable sequences, typically used for cases where
an immutable sequence of homogeneous data is needed.
'''

t = ()					# Empty tuple
print(t)
t = (10)				# int
u = (10,)				# 1-element tuple
print(t, u)
t = ('a', 'b', 'c', 'd')
t += ('d',)
print(t)
u = (0,) * 5
print(u)

print('a' in t, 'A' in t, "A" not in t)
print(t[0])
print(t[1:3])

#t[1] = 'B'		# TypeError: 'tuple' object does not support item assignment

print(len(t))
print(min(t))
print(max(t))
print(t.index('d', 0, 4))
print(t.count('d'))

(one, two, three) = (11, 22, 33)
print(one, two, three)
one, two, three = 111, 222, 333
print(one, two, three)

a = 2;  b = 3
a, b = b, a				# Swap x and y
print(a, b)

t = (1, 2, 3, 4, 5)
*a, b, c  =  t			# a = [1, 2, 3]
print(a, b, c)
a, *b, c  =  t			# b = [2, 3, 4]
print(a, b, c)
a, b, *c  =  t			# c = [3, 4, 5]
print(a, b, c)

l = list(t)
print(l)
t = tuple(l)
print(t)



'''
A set object is an unordered collection of distinct hashable objects. Common
uses include membership testing, removing duplicates from a sequence, and
computing mathematical operations such as intersection
'''

print()
s = {}
print(s)
s = {5, 2, 8, 9, 1, 5, 8}
print(s)

print(8 in s, 10 in s, 10 not in s)
#print(s[0])		# TypeError: 'set' object is not subscriptable
#print(s[1:3])		# TypeError: 'set' object is not subscriptable

print(len(s))
print(min(s))
print(max(s))

s.add(3)
s.remove(8)
print(s)

r = {1, 2, 3, 4}
print(s | r)
print(s & r)
print(s ^ r)

print(r < s, {1, 2} < s)		# Proper subset
print(r <= r)					# Subset

print(s.pop(), s.pop())		# Remove and return an arbitrary element from the set
print(s)
