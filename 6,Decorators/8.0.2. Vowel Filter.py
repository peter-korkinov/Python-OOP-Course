def vowel_filter(function):
    def wrapper():
        vowels = ["a", "e", "o", "u", "i"]
        return [letter for letter in function() if letter in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
