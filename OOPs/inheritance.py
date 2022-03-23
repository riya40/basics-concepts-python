class City:
    def street(self):
        print("xyz line")


class Street(City):
    def line_no(self):
        print("line no 4 ijn c street")


_street = Street()
_street.line_no()
_street.street()


# multiple inheritance
class State:
    def place(self):
        print("this first parent class")
        print("this is state")


class City:
    def street(self):
        print("xyz line")


class Street(State, City):
    def line_no(self):
        print("in multiple line no 4 ijn c street")


_street_ = Street()
_street_.line_no()


# multilevel inheritence
class State:
    def place(self):
        print("this first parent class")
        print("this is state")


class City(State):
    def street(self):
        print("xyz line")


class Street(City):
    def line_no(self):
        print("in multiple line no 4 ijn c street")


_street_line = Street()
_street_line.line_no()
_street_line.street()
_street_line.place()


# hireraichal inheritence
class Vehicle:
    def info(self):
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self):
        print("Car class")


class Truck(Vehicle):
    def truck_info(self):
        print("Truck class")


_car = Car()
_car.info()
_car.car_info('BMW')

_truck = Truck()
_truck.info()
_truck.truck_info('Ford')
