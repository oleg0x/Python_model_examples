#! /usr/bin/python

'''
Dictionary is a mutable object which maps hashable values to
arbitrary objects.
'''

d = {}				# Empty dict
print(d)

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['two', 'one', 'three'], [2, 1, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a)
print(a == b == c == d == e == f)

d["four"] = 4
print(d)
#print(d["xxx"])		# KeyError exception if key is not in the map

print(len(d))

d2 = {(1,1,1): 10, (1,2,3): 15}		# Dict of elements (tuple, int)
d2[(9,8,7)] = 20
print((1,2,3) in d2, (4,5,6) in d2, (4,5,6) not in d2)

d2 = d.copy();
del d2["two"]
d2["aaa"] = None
print(d)
print(d2)
d2.update({"one": 111, "three": 333, "five": 5})
print(d2)
print(d2.pop("one", 0))		# If key is in the dict, remove it and return its value, else return default
print(d2)
d2.clear()
print(d2)

print(d.get("three", 0), d.get("xxx", 0), d.get("xxx"))
print(d.setdefault("three", 0), d.setdefault("xxx", 0))

keys = d.keys()		# When the dict changes, the view reflects these changes
vals = d.values()
print(list(keys), list(vals))
del d["one"]
print(list(keys), list(vals))

s = "aaa bbb aaa ccc aaa ccc"
occurences = {}
for word in s.split():
	occurences[word] = occurences.get(word, 0) + 1
for word in occurences:
	print(word, occurences[word])
for (word, n) in occurences.items():		# The same as previous 'for'
	print(word, n)
