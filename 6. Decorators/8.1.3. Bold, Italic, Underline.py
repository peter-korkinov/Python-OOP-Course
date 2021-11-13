def make_bold(deco_func):
    def layer_1(*args):
        return f"<b>{deco_func(*args)}</b>"
    return layer_1


def make_italic(deco_func):
    def layer_1(*args):
        return f"<i>{deco_func(*args)}</i>"
    return layer_1


def make_underline(deco_func):
    def layer_1(*args):
        return f"<u>{deco_func(*args)}</u>"
    return layer_1


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
