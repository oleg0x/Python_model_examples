class MyClass:
	pass

MyClass.x = 10
MyClass.s = "abcde"
print(MyClass.x, MyClass.s)



class MyClass2:
	def __init__(self):
		self.a = 42

circle = MyClass2()					# Instance of the class
print(circle.a)



class Circle1:
	pi = 3.14159					# Class variable

	def __init__(self, r=1):
		self.radius = r

	def area(self):
		return Circle1.pi * self.radius * self.radius

print("Circle1.pi =", Circle1.pi)
c1 = Circle1()
c2 = Circle1(10)
print(c1.area(), c2.area())



class Circle2:
	pi = 3.14159					# Class variable
	all_circles = []				# Class variable

	def __init__(self, r=1):
		self.radius = r
		__class__.all_circles.append(self)

	def area(self):
		return __class__.pi * self.radius * self.radius

	@staticmethod
	def total_area():				# Static method
		total = 0
		for c in __class__.all_circles:
			total += c.area()
		return total

	@classmethod
	def total_area(cls):			# Class method
		total = 0
		for c in cls.all_circles:
			total += c.area()
		return total

c1 = Circle2(10)
c2 = Circle2(20)
print("Total area:", Circle2.total_area())



class Shape:
	s = "Shape"
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def move(self, delta_x, delta_y):
		self.x += delta_x
		self.y += delta_y

class Square(Shape):
	def __init__(self, x=0, y=0, side=1):
		Shape.__init__(x, y)
		self.side = side

class Circle(Shape):
	def __init__(self, x=0, y=0, r=1):
		super().__init__(x, y)
		self.radius = r

c = Circle(1, 1, 10)
c.move(5, 6)
print(c.x, c.y)
print(Shape.s, Square.s, c.s)
Square.s = "Square"					# New variable in Square is created
c.s = "Circle"						# New variable in Circle is created
print(Shape.s, Square.s, c.s)



class SomeClass:
	def __init__(self):
		self.x = 100
		self.__y = 0				# Private variable

	def some_method(self):
		self.__update_y()
		print(self.__y)

	def __update_y(self):
		self.__y = 42

sc = SomeClass()
print(sc.x)							# OK, x is public variable
#print(sc.__y)						# Error: object has no attribute '__y'
print(sc._SomeClass__y)				# But it is OK with prefix '_SomeClass'
#sc.__update_y()					# Error: object has no attribute '__update_y'
sc._SomeClass__update_y()			# But it is OK with prefix '_SomeClass'
sc.some_method()



class Temperature:
	def __init__(self):
		self._temp_fahr = 0

	@property
	def temp(self):					# Property 'temp'
		return (self._temp_fahr - 32) * 5 / 9

	@temp.setter
	def temp(self, new_temp):		# Set-method for the property 'temp'
		self._temp_fahr = new_temp * 9 / 5 + 32

t = Temperature()
print(t._temp_fahr, t.temp)
t.temp = 20
print(t._temp_fahr, t.temp)
