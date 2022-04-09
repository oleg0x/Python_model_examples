def fact(n):
	"""Calculate the factorial of a number."""
	res = 1					# Local variable
	while n > 0:
		res = res * n
		n -= 1
	return res

print(fact.__doc__, fact(5))



def some_func1(a, b, c):
	return a * b + c

print(some_func1(10, 3, 5))
#someFunc1(10, 3)			# TypeError: missing 1 required positional argument



def some_func2(a, b=1, c=0):			# Default argument values
	return a * b + c

print(some_func2(10, 3, 5))
print(some_func2(10))					# Using default argument values
print(some_func2(b=3, c=5, a=10,))		# Using keyword arguments



def some_func3(k, *nums):
	if len(nums) == 0:
		return None
	else:
		return k * sum(nums)

print(some_func3(2))
print(some_func3(2, 10, 20, 30))



def some_func4(x, y, **other):
	print("x: {0}, y: {1}, keys in 'other': {2}".format(x, y, list(other.keys())))
	print("Sum of 'other:'", sum(other.values()))

some_func4(2, 3, foo=100, bar=200)



def some_func5(n, str1, list1, list2):
	n += 100						# Doesn't change outside var
	str1 = "New_string"				# Doesn't change outside string
	list1.append(3)					# Changes outside list
	list2 = [100, 200, 300]			# Doesn't change outside list

n = 42
str1 = "Some_string"
l1 = [1, 2]
l2 = [10, 20]
some_func5(n, str1, l1, l2)
print(n, str1, l1, l2)



def some_func6():
	global a
	a = 10				# Changes outside global var
	b = 20				# Doesn't change outside var

a = "one"
b = "two"
some_func6()
print(a, b)



str2func = {"aaa": some_func1, "bbb": some_func2, "ddd": some_func4}
str2func["ddd"](42, 43, foo=44)



func_list = [lambda a, b: (a + b) * 2, lambda a, b: (a + b) / 2]
print(func_list[0](2, 3), func_list[1](5, 7))



def even(n):
	i = 2
	while i <= n:
		yield i
		i += 2

for i in even(16):
	print(i, end=' ')
print()



def decorate(func):
	print("In decorate function, decorating", func.__name__)
	def wrapper_func(*args):
		print("Executing", func.__name__)
		return func(*args)
	return wrapper_func

@decorate
def myfunc(param):
	print(param)

myfunc("Hello!")
