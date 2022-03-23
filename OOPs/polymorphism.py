"""
polymorphism means that can perform task in different forms
polymorphism can perform in 2 ways:
  1)method overriding and
  2)method overloading
Method Overriding:in this having same methods in different classes
Method Overloading:in this having the same methods but have different parameters
"""


class Livingthings:  # parent class
    def omnivores(self):
        things = "animals"
        print(things)


class Spices(Livingthings):  # child class
    def ominivores(self):
        things = "humans"
        return things


values = Spices()
print(values.ominivores())


#method overloading
class Institutions:
    def college(self, name=None):
        if not name:
            print("college:" + name)
        else:
            print("pragati college")


values = Institutions()
values.college()
values.college("aditya")


