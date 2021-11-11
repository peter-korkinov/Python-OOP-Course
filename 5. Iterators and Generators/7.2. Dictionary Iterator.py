# class dictionary_iter:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary
#
#     def __iter__(self):
#         for i in self.dictionary.items():
#             yield i

class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        listed_dict = [tup for tup in self.dictionary.items()]
        if self.index < len(listed_dict):
            temp = listed_dict[self.index]
            self.index += 1
            return temp
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
