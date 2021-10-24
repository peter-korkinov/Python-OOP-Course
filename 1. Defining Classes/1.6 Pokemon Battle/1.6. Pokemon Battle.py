class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon_name):
        if pokemon_name in self.pokemon:
            return "This pokemon is already caught"
        else:
            self.pokemon.append(pokemon_name)
            return f"Caught {pokemon_name.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for i in self.pokemon:
            if not pokemon_name == i.name:
                return "Pokemon is not caught"
            else:
                self.pokemon.remove(i)
                return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemon_returns_list = []
        for i in self.pokemon:
            pokemon_returns_list.append(f"- {i.pokemon_details()}")
        temp_string = "\n".join(pokemon_returns_list)

        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemon)}\n" \
               f"{temp_string}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
