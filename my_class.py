class MyClass:

	def __init__(self, name, number):
		self.name = name
		self.number = number

	def to_string(self):
		return "I am " + self.name + ", " + str(self.number)

myc = MyClass("Bill", 19)
yourc = MyClass("Sam", 11)

print myc.to_string()
print yourc.to_string()