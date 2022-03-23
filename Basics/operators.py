def arithmetic_operators_example(a, b):
    """
    performs the operations
    :param a:
    :param b:
    :return:
    """
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    modu = a % b
    expo = a ** b
    floordiv = a // b
    print(add, sub, mul, div, modu, expo, floordiv)


def assignment_operators_example(a, b):
    """
    performing the operation and Assigning the value
    :param a:
    :param b:
    :return:
    """
    a += b
    print(a)
    a -= b
    print(a)
    a *= b
    print(a)
    a /= b
    print(a)
    a %= b
    print(a)
    a **= b
    print(a)
    a //= b
    print(a)


def bitwise_operators_example(a, b):
    """
    operation that perfrom on bits
    :param a:
    :param b:
    :return:
    """
    print(a & b)
    print(a | b)
    print(~a)
    print(a ^ b)
    print(a >> 2)
    print(a << 2)


if __name__ == '__main__':
    a = int(input("enter first value"))
    b = int(input("enter second value"))
    arithmetic_operators_example(a, b)
    assignment_operators_example(a, b)
    bitwise_operators_example(a, b)
