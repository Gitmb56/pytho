# Prectice Object Orianted  Programme...........
class Lalita:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def behaviour(self):
        return "very sensitive girl"

    def work(self):
        return "housewife"


my_wife = Lalita("Lalita", 22, "married")
print(my_wife.behaviour())
