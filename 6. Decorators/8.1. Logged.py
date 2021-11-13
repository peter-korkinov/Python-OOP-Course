from functools import wraps


# def logged(*args):
#     def decorator(function, *args):
#         @wraps(function)
#         def wrapper(*func_input):
#             return f"you called {function.__name__}({func_input})\n" \
#                    f"it returned {function(func_input)}"
#         return wrapper
#     return decorator


def logged(decorated_func):
    def wrapper(*args):
        fun = decorated_func(*args)
        result = f"you called {decorated_func.__name__}{args}\n" \
                 f"it returned {fun}"
        return result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
