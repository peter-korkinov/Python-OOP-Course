class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        temp = ""
        for key, value in self.skills.items():
            temp += f"==={key} - {value}\n"
        # temp = temp[:-2]

        return f"Name: {self.name}\n" \
               f"Guild: {self.guild}\n" \
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n" \
               f"{temp}"


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.add_skill("Shield Break", 20))
# print(player.add_skill("cunt smash", 20))
# print(player.player_info())
