from abc import ABC
"""Abstract methods do not contain their implementation"""


class Place(ABC):
    def line(self):
        pass


class Street(Place):
    def line(self):
        print("The Xyz line in abc count situated in north-west")


obj = Street()
obj.line()