#! /usr/bin/python

try:				# Possibly throwing block
	a, b = 100, 20
	x = a / b
	something_bad = True
	if something_bad:
		raise RuntimeError("Something went wrong.")

except ZeroDivisionError:
	print("Division by 0!")
except RuntimeError as rte:
	print("Runtime error!", rte)
except:				# All other exceptions
	print("Other exception!")
else:				# Only if there was no exception in 'try' block
	print("Everything was OK, no exceptions.")
finally:			# Always after 'try', 'except' and 'else'
	# Clear variables, close files and so on
	print("Final steps.")



class MyException(Exception):
	pass

try:
	x = 42
	y = 123.45
	raise MyException("Some information about what went wrong.", x, y)

except MyException as my_ex:
	print("Situation: {0}\n x = {1}, y = {2}".format(my_ex.args[0],
		my_ex.args[1], my_ex.args[2]))



s = "abcde"
assert len(s) > 3, "'s' is too short!"



with open("file1.txt") as infile:
	data = infile.read()
