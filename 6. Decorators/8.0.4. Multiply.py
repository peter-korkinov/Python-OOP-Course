from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(n):
            func = function(n)
            return func * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
print(add_ten.__name__)

# @multiply(5)
# def add_ten(number):
#     return number + 10
#
#
# print(add_ten(6))
