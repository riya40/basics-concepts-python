from functools import reduce
"""
lambda:it is keyword that can helps in define functions it can reduce the code
map:it can apply on every value and it converts into list 
filte:it returns the fltres value
reduce:it can applies in every item and returns the value
"""


def sqauare(n):
    return n ** 2


square = lambda n: n ** 2
print(sqauare(3))

squares = list(map(lambda n: n ** 2, range(1, 10, 2)))

num1 = [2, 4, 9]
num2 = [3, 8, 5]
result = list(map(lambda x, y: x + y, num1, num2))
print(result)
result1 = list(filter(lambda x, : x % 2 != 0, num1))
print(result1)
result2 = reduce(lambda x, y: x + y, num2)
print(result2)
