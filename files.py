#! /usr/bin/python

file_name = "data.txt"

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
f = open(file_name)					# f is file object
f = open(file_name, "rt")			# The same, "rt" means 'read text'
f.close()

try:
	f = open(file_name, "rt")
	str = f.read(20);				# Read at most 20 characters
finally:
	f.close();
print(str)

# Equivalent to previous, except f.read()
with open(file_name, "rt") as f:	# 'With' statement context manager
	str = f.read();					# Read entire file
	# f is closed here
print(str)

with open(file_name, "rt") as f:	# f = open(file_name) is the same
	line1 = f.readline()			# Read one line including '\n'
	line2 = f.readline()
print(line1, line2, sep='')

with open(file_name, "rt") as f:
	lines = f.readlines();
print(lines)
print()

f = open(file_name)
count = 0
for line in f:						# For loop with file object
	count += 1
	print(count, ") ", line, sep='', end='')
f.close()
print()

f = open("new_data.txt", "wt")
f.write("First line\n");			# No '\n' automatically at the end of line
f.write("Second line\n");
li = ["aaa\n", "bbb\n", "ccc"]		# No '\n' automatically at the end of each line
f.writelines(li)
f.close()

nums = [50, 60, 70, 80, 90]			# Bytes only
barr = bytearray(nums)
outf = open("data.bin", "wb")	# "wb" means 'write binary'
outf.write(barr)
outf.close()

inf = open("data.bin", "rb")
li = list(inf.read())
print(li)
