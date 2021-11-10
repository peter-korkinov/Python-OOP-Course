from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.sound = "Hoot Hoot"
        self.food_preferences = ["Meat"]
        self.weight_gain = 0.25


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.sound = "Cluck"
        self.food_preferences = ["Meat", "Vegetable", "Fruit", "Seed"]
        self.weight_gain = 0.35
