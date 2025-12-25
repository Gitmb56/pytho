# Prectice Object Orianted  Programme...........
class Cat:
	def __init__(self,name,age,color):
		self.name = name
		self.age = age 
		self.color = color
	def sound(self):
		return f"my name is {self.name} (Meow)..age {self.age} my color {self.color}"
    def all_fun_prec(self):
		for i in range(0,11):
			print(i)
d = Cat("Pushe",2,"gray shadow")

print(d.sound())
#print(d.__dict__)
#print(" This is a class dict ..........")
#print(Cat.__dict__)