from creatureClass import Creature
import skillClass as sklz
import random

class Summon(Creature):
    def __init__(self, creature_name, description: str, creature_actions: list, hp: int, danger_level, controlled: bool):
        self.creature_name = creature_name
        self.description = description
        self.creature_actions = creature_actions
        self.hp = hp
        self.danger_level = danger_level
        self.controlled = controlled
        
    
        
        
        
octopus_fey = Summon("Grizzly Octopus", "a fur-covered octopus that prominently displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 30, 1, True)

#option_print_iter("Will you control the summon? Will it control itself?", ("have a controlled summon", "have an independent summon"), 2)
