class Study:
    """
    class is a "blueprint" for creating objects.
    An object is the collection of various data and functions that operate on those data
    """
    def standard(self):
        print("the student studying 6th standard")


study_ = Study()  # object creation
study_.standard()


# encapsulation
class Degrees:
    """
    Encapsulation that wrap up the datamebers and methods into a single unit
    """

    def __init__(self, ug, pg):  # data memebers
        self.ug = ug
        self.pg = pg

    def pc(self):  # methods to shows the data
        print("UGs and PGs are:", self.ug, self.pg)


_degree = Degrees("B tech", "M tech")
_degree.pc()
