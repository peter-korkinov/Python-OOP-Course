class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        elif price > self.__budget:
            return "Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_summed = 0
        for worker in self.workers:
            salaries_summed += worker.salary

        if self.__budget >= salaries_summed:
            self.__budget -= salaries_summed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_cost = 0
        for animal in self.animals:
            tending_cost += animal.get_needs()

        if self.__budget >= tending_cost:
            self.__budget -= tending_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_str = ""
        tigers_str = ""
        cheetahs_str = ""

        lions_amount = 0
        tigers_amount = 0
        cheetahs_amount = 0

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions_str += f"{animal.__repr__()}\n"
                lions_amount += 1
            elif animal.__class__.__name__ == "Tiger":
                tigers_str += f"{animal.__repr__()}\n"
                tigers_amount += 1
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs_str += f"{animal.__repr__()}\n"
                cheetahs_amount += 1

        return f"You have {len(self.animals)} animals\n" \
               f"----- {lions_amount} Lions:\n" \
               f"{lions_str}" \
               f"----- {tigers_amount} Tigers:\n" \
               f"{tigers_str}" \
               f"----- {cheetahs_amount} Cheetahs:\n" \
               f"{cheetahs_str[:-1]}"

    def workers_status(self):
        caretakers_str = ""
        keepers_str = ""
        vets_str = ""

        caretakers_amount = 0
        keepers_amount = 0
        vets_amount = 0

        for worker in self.workers:
            if worker.__class__.__name__ == "Caretaker":
                caretakers_str += f"{worker.__repr__()}\n"
                caretakers_amount += 1
            elif worker.__class__.__name__ == "Keeper":
                keepers_str += f"{worker.__repr__()}\n"
                keepers_amount += 1
            elif worker.__class__.__name__ == "Vet":
                vets_str += f"{worker.__repr__()}\n"
                vets_amount += 1

        return f"You have {len(self.workers)} workers\n" \
               f"----- {keepers_amount} Keepers:\n" \
               f"{keepers_str}" \
               f"----- {caretakers_amount} Caretakers:\n" \
               f"{caretakers_str}" \
               f"----- {vets_amount} Vets:\n" \
               f"{vets_str[:-1]}"