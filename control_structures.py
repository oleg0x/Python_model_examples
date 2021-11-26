#! /usr/bin/python

x = 0
if x < 1: pass
else: x = 1
print(x)

x = -5
if x > 0:
	print("Positive")
elif x < 0:
	print("Negative")
else:
	print("Zero")

i = 0
while i < 5:
	print(i, end=' ')
	i += 1
print()

i = 0
while i < 20:
	i += 1
	if i % 4 == 0: continue
	if i % 15 == 0: break
	print(i, end=' ')
else:
	print("Some message")
print()

nums = [10, 20, 30, 40, 50, 60]

for x in nums:
	print(x*x, end=' ')
print()

for i, n in enumerate(nums):
	print(i, n, end=' ')
print()

for i in range(len(nums)):
	print(i, nums[i], end=' ')
print()

for i in range(5, 10):			# [start, stop)
	print(i, end=' ')
print()

for i in range(10, 0, -1):		# range(start, stop, step)
	print(i, end=' ')
print()

li = [(1, 2), (3, 4), (5, 6)]
res = 0;
for x, y in li:
	res += x * y
print(res)						# res = 1*2 + 3*4 + 5*6 = 44

chars = ['a', 'b', 'c']
z = zip(nums, chars)
print(list(z))

squared = [x**2 for x in range(10)]		# List comprehension
print(squared)

nums_squared = [x*x for x in nums if x % 20 == 0]
print(nums_squared)

nums_squared = [x+1 for x in nums if x >= 30]
print(nums_squared)

nums_sq_dict = {x: x*x for x in nums if x % 20 == 0}	# Dict comprehension
print(nums_sq_dict)

nums_sq = (x*x for x in nums)		# Can be used in 'for'
print(nums_sq)
for x in nums_sq:
	print(x, end=' ')
print()
