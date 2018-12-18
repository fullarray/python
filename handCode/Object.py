class Person:
	distance = 0
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age
	
	def __str__(self):
		return self.firstname + " " + self.lastname +", "+ str(self.age)
		
	def setFirst(self, first):
		self.firstname = first

	def setLast(self, last):
		self.lastname = last
	
	def jumps(self, distance):
		self.distance = distance
		print ("Jumps : "+ str(self.distance) +" meters")
	
class Employee(Person):
	def __init__(self, first, last, age, emplid):
		super().__init__(first, last, age)
		self.staffno = emplid
	
	def __str__(self):
		return "Employee: "+ super().__str__() + ", " + str(self.staffno)


person1 = Person("John", "Ray", 60);
person1.setFirst('Mark')
person1.setLast('Smith')

employee1 = Employee("Maria", "Morales", 50, 44555)
person1.jumps(20)
employee1.jumps(30)
print(person1)
print(employee1)
