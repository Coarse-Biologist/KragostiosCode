import skillClass as sklz

class Creature:

    def __init__(self, creature_name, description: str, creature_actions: list, hp: int, danger_level):

        self.creature_name = creature_name

        self.description = description

        self.creature_actions = creature_actions

        self.hp = hp

        self.danger_level = danger_level

    def check_environment(self):
        print(f"{self.creature_name}) is frantically scanning its surroundings.")
        
        
octopus_feyAlpha = Creature("Alpha Grizzly Octopus", "A fur-covered octopus that prominently displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 40, 1)

octopus_fey = Creature("Grizzly Octopus", "A fur-covered octopus that displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 30, 1)


octopus_feyBeta = Creature("Beta Grizzly Octopus", "A fur-covered octopus that insecurely displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 25, 1)





 