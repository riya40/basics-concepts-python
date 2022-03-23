def predefined_exception():
    try:
        a = int(input('enter a '))
        b = int(input('enter b '))
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("zero is not divisible")


def custom_exception():
    class Error(Exception):
        """Base class for other exceptions"""
        pass

    class UnderRage(Error):
        """Raised when the input value is below 18"""
        pass

    try:
        age = int(input("Enter the age for eligibility "))
        if age < 18:
            raise UnderRage
        print("The Enter Age is Suitable for Vote: {}".format(age))
    except UnderRage:
        print("The Enter Age is Not Suitable for Vote")


if __name__ == '__main__':
    predefined_exception()
    custom_exception()