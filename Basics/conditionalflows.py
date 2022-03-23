def example_for_loop():
    """
    The for loop that iterates the block of the code
    if its condition satifies
    :return:
    """
    table = 2
    for i in range(1, 13):
        result = table * i
        print({table}, "*", {i}, "=", {result})


def function_whileloop():
    """
    the While loop that enter into the loop if condition is satifies and perform the operation or
    if condition not satifies it exists from the loop
    :return:
    """
    i = 1
    while i <= 5:
        value = i ** 2
        print(value, "is the 2 power of", i)
        i = i + 1


def example_if_condition():
    a = 10
    b = 5
    c = 15
    if a > b and a > c:  # comparison operator and logical operator example
        print("a is small")
    elif b > a and b > c:
        print("b is big")
    else:
        print("c is big")


if __name__ == '__main__':
    function_whileloop()
    example_if_condition()
    example_for_loop()
