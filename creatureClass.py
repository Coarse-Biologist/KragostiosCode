import skillClass as sklz

class Creature:

    def __init__(self, creature_name, description: str, creature_actions: list, hp: int, danger_level):

        self.creature_name = creature_name

        self.description = description

        self.creature_actions = creature_actions

        self.hp = hp

        self.danger_level = danger_level

    #def use_environment(self, the_environment): # creatureClass skill
    # if the_environment == "jungle":
    #     self.creature_actions.append(sklz.climb())
    # elif the_environment == "cliffs":
    # elif the_environment == "forest":
    # elif the_environment == "canyons":
    # elif the_environment == "grasslands":
    # elif the_environment == "icy terrain":
    # elif the_environment == "muddy terrain":
    # elif the_environment == "subterranean caves":
    # elif the_environment == "quick sand":
    # elif the_environment == "barren wasteland":
    # elif the_environment == "cactus-filled desert":
    # elif the_environment == "deserted village":
    # elif the_environment == "a slowly flowing river":
    # elif the_environment == "a treacherously fleet snd rocky river":
        
octopus_feyAlpha = Creature("Alpha Grizzly Octopus", "A fur-covered octopus that prominently displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 40, 1)

octopus_fey = Creature("Grizzly Octopus", "A fur-covered octopus that displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 30, 1)


octopus_feyBeta = Creature("Beta Grizzly Octopus", "A fur-covered octopus that insecurely displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 25, 1)





 