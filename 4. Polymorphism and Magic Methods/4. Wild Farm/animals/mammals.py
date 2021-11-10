from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.sound = "Squeak"
        self.food_preferences = ["Vegetable", "Fruit"]
        self.weight_gain = 0.10


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.sound = "Woof!"
        self.food_preferences = ["Meat"]
        self.weight_gain = 0.40


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.sound = "Meow"
        self.food_preferences = ["Vegetable", "Meat"]
        self.weight_gain = 0.30


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.sound = "ROAR!!!"
        self.food_preferences = ["Meat"]
        self.weight_gain = 1
