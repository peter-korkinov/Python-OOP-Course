def type_check(input_type):
    def layer_1(func):
        def layer_2(num):
            if type(num) is input_type:
                return func(num)
            else:
                return "Bad Type"
        return layer_2
    return layer_1


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
