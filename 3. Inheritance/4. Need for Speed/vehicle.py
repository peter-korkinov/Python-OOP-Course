class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = float(1.25)
    fuel_consumption = float
    fuel = float
    horse_power = int

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if self.DEFAULT_FUEL_CONSUMPTION * kilometers <= self.fuel:
            self.fuel -= self.DEFAULT_FUEL_CONSUMPTION * kilometers
