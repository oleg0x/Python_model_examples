#! /usr/bin/python

n = 555555555555555555555555555555555555555555555555555555  # Long number
print(n)

r = 5 / 3						# float
print(r, type(r))
n = 5 // 3						# int
print(n, type(n))
print(11 % 3)
k, r = divmod(20, 3)
print(k, r)

print(abs(-123))
print(int(9.678), round(9.678))

print(pow(2, 10), 2**10)

print(2 + 3 == 5, 5 > 10)

nums = (5, -7, 2, 8, -3)
print(nums)
a, b, s = min(nums), max(nums), sum(nums)
print("Min number:", a, "| Max number:", b, "| Sum:", s)

# Complex numbers
print()
z1 = 2 + 4j
print(z1.conjugate())
z2 = complex(5, -1)
print(z1 + z2, z1 * z2)
z = 1j * 1j						# j^2= -1
print(z.real, z.imag)

import math						# Mathematical functions for real numbers
import cmath					# Mathematical functions for complex numbers

print()
print(math.factorial(5))
print(math.gcd(20, 30))			# Greatest common divisor of the integers
#print(math.lcm(20, 30))		# Least common multiple of the integers
x = 100
print(math.isfinite(x), math.isinf(x), math.isnan(x))
print(math.prod((3, 10, -2, 5)))

print()
print(math.sqrt(10000))
print(math.exp(4))
print(math.log2(512), math.log(81, 3))


print()
print(math.cos(math.pi))
print(math.atan(1.0))			# = Pi/4
print(math.sinh(3))

print()
print(math.e, math.pi)
print(-math.inf, math.nan, math.inf)		# not a number, infinity

print()
print(cmath.phase(-1+0j))
z = 2 + 3j
print(cmath.exp(z))
print(cmath.tan(z))
