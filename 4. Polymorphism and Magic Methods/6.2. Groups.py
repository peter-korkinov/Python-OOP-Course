class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(None, self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

    def __repr__(self):
        people_stringed = ", ".join([pers.__repr__() for pers in self.people])
        return f"Group {self.name} with members {people_stringed}"


# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
#
# print(len(first_group))
# print(second_group)
# print(third_group[0])
#
# for person in third_group:
#     print(person)
