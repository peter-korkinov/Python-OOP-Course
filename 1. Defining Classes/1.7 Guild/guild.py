from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.players_names = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            player.guild = self.name
            self.players.append(player)
            self.players_names.append(player.name)
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name in self.players_names:
            playa = None
            for i in self.players:
                if i.name == player_name:
                    playa = i
                    break
            playa.guild = "Unaffiliated"
            self.players.remove(playa)
            self.players_names.remove(player_name)
            return f"Player {player_name} has been removed from the guild."

        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        temp = ""
        for plr in self.players:
            temp += f"{plr.player_info()}\n"
        # temp = temp[:-2]

        return f"Guild: {self.name}\n" \
               f"{temp}"


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
# print(guild.kick_player("George"))
# print(guild.kick_player("George"))
#
# guild = Guild("GGXrd")
# player = Player("Pesho", 90, 90)
# player.add_skill("A", 3)
# player.guild = "kuche"
# print(guild.assign_player(player))
#
# # print(guild.assign_player(player))
# # print(guild.assign_player(player))
# # print(player.player_info())
# print(player.player_info())