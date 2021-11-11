class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iteration = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration <= self.number:
            if self.index == len(self.sequence):
                self.index = 0
            current_output = self.sequence[self.index]
            self.index += 1
            self.iteration += 1
            return current_output
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
