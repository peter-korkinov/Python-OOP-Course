def even_parameters(deco_func):
    def layer_1(*args):
        for i in args:
            if type(i) is int:
                if not i % 2 == 0:
                    return "Please use only even numbers!"
            else:
                return "Please use only even numbers!"
        return deco_func(*args)
    return layer_1


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
