class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.iteration < self.count:
            n = self.number
            self.number += self.step
            self.iteration += 1
            return n
        raise StopIteration


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)