def first_arguments(value):
    """
    only we give the single argument
    :param value:
    :return:
    """
    num = 5
    num = num * value
    print("value is:{}".format(num))


def function_args(*args):
    """
    when you have an indefinite number of arguments.
    param args:
    :return:value in Tuples
    """
    for items in args:
        print("values are:{}".format(items))


def function_kwargs_example(**kwargs):
    """
    **kwargs when you have an indefinite number of keyword arguments
    :param kwargs:
    :return:
    """
    for keys, values in kwargs.items():
        print("the keys is",  {keys}, "and their values is:", {values})


if __name__ == '__main__':
    first_arguments(5)
    values = ["priya", "sankar", "tripura"]
    function_args(*values)
    dic = {"one": "hello", "two": "python"}
    function_kwargs_example(**dic)
