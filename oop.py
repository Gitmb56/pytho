# Prectice Object Orianted  Programme...........
class Lalita:
    def __init__(self,name,age,status):
		self.name=name
		self.age=age
		self.status=status
    def behaviour(self):
            return f"very sensitive girl"
    def work(self):
            return f"housewife"

my_wife = Lalita("Lalita",22,married)
my_wife.behaviour()